import logging
import os
from pathlib import Path
from typing import Any, Optional, TextIO, Union

from loguru import logger
from rich.logging import RichHandler


EMMA_LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG").upper())

LOGGER_FORMAT = (
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)
RICH_TRACEBACK_SUPPRESS_MODULES = ("starlette", "click", "uvicorn", "fastapi")


class PropagateHandler(logging.Handler):
    """Logger handler to send logs to the `logging` module."""

    def emit(self, record: logging.LogRecord) -> None:
        """Emit method for logging."""
        logging.getLogger(record.name).handle(record)


class InterceptHandler(logging.Handler):
    """Logger Handler to intercept log messages from all callers."""

    def emit(self, record: logging.LogRecord) -> None:
        """Emit method for logging."""
        # Get corresponding Loguru level if it exists
        level: Union[str, int]

        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2

        while frame.f_code.co_filename == logging.__file__:
            if frame.f_back is not None:
                frame = frame.f_back
                depth += 1

        logger.bind(**self._bind(record)).opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )

    def _bind(self, record: logging.LogRecord) -> dict[str, Any]:
        """Add kwargs to the logged output."""
        return {}


def setup_logging(
    sink: Union[logging.Handler, str, Path, TextIO],
    root_handler: Optional[logging.Handler] = None,
    log_level: str = "INFO",
    emma_log_level: Optional[str] = None,
) -> None:
    """Setup a better logger.

    If you want to log EMMA modules separately, provide a log level for the `emma_log_level`.
    """
    if not root_handler:
        root_handler = InterceptHandler()

    if log_level:
        log_level = log_level.upper()

    if emma_log_level:
        emma_log_level = emma_log_level.upper()

    # intercept everything at the root logger
    logging.root.handlers = [root_handler]
    logging.root.setLevel(logging.getLevelName(log_level))

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

        # Get the log for the emma modules separately
        if name.startswith("emma_") and emma_log_level:
            logging.getLogger(name).setLevel(emma_log_level)

    # configure loguru
    logger.configure(
        handlers=[
            {
                "sink": sink,
                "format": LOGGER_FORMAT,
            }
        ]
    )


def setup_rich_logging(
    log_level: str = "INFO",
    emma_log_level: Optional[str] = None,
    rich_traceback_show_locals: bool = True,
    rich_traceback_suppress_modules: tuple[str, ...] = RICH_TRACEBACK_SUPPRESS_MODULES,
    rich_handler_kwargs: Optional[dict[str, Any]] = None,
) -> None:
    """Setup logging with Rich as default."""
    # Default o an empty dict if there are no kwargs provided
    if not rich_handler_kwargs:
        rich_handler_kwargs = {}

    rich_handler = RichHandler(
        markup=True,
        rich_tracebacks=True,
        tracebacks_show_locals=rich_traceback_show_locals,
        tracebacks_suppress=rich_traceback_suppress_modules,
        **rich_handler_kwargs
    )
    return setup_logging(sink=rich_handler, log_level=log_level, emma_log_level=emma_log_level)
