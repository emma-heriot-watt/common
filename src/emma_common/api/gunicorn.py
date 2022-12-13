from __future__ import annotations

import logging
import os
from typing import Any

from loguru import logger

from emma_common.logging import InterceptHandler


try:  # noqa: WPS229
    from fastapi import FastAPI
    from gunicorn.app.base import BaseApplication
    from gunicorn.glogging import Logger
except ImportError:
    logger.warning(
        "gunicorn is not installed. If you are using this module, you likely want to install emma-common with the `api` group."
    )


LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "INFO").upper())


class GunicornLogger(Logger):  # type: ignore[misc]
    """Logger class for Gunicorn."""

    def setup(self, cfg: Any) -> None:
        """Setup the gunicorn loggers to use loguru."""
        log_handler = InterceptHandler()

        self.error_logger = logging.getLogger("gunicorn.error")
        self.error_logger.addHandler(log_handler)
        self.access_logger = logging.getLogger("gunicorn.access")
        self.access_logger.addHandler(log_handler)
        self.error_logger.setLevel(LOG_LEVEL)
        self.access_logger.setLevel(LOG_LEVEL)


class StandaloneApplication(BaseApplication):  # type: ignore[misc]
    """Gunicorn application."""

    def __init__(self, app: Any, options: dict[Any, Any] | None = None) -> None:
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self) -> None:
        """Load the gunicorn config."""
        if not self.cfg:
            return

        for name, setting_value in self.options.items():
            if name not in self.cfg.settings:
                continue
            if setting_value is None:
                continue
            self.cfg.set(name.lower(), setting_value)

    def load(self) -> Any:
        """Load the application."""
        return self.application


def create_gunicorn_server(
    app: FastAPI, host: str, port: int, workers: int, **kwargs: dict[str, Any]
) -> StandaloneApplication:
    """Create a gunicorn server for the API app."""
    server_config = {
        "bind": f"{host}:{port}",
        "workers": workers,
        "accesslog": "-",
        "errorlog": "-",
        "worker_class": "uvicorn.workers.UvicornWorker",
        "logger_class": GunicornLogger,
        **kwargs,
    }
    server = StandaloneApplication(app, server_config)
    return server
