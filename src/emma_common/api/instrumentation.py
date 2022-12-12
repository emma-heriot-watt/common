"""Easily instrument and handle tracing for FastAPI.

This module makes handling instrumentation for observability much easier. This will only work
providing the relevant packages are installed. If they're not installed, the various functions will
do nothing.
"""

from __future__ import annotations

from fastapi import FastAPI
from loguru import logger


try:  # noqa: WPS229
    from opentelemetry import trace  # noqa: WPS433
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (  # noqa: WPS433
        OTLPSpanExporter,
    )
    from opentelemetry.instrumentation.botocore import BotocoreInstrumentor  # noqa: WPS433
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor  # noqa: WPS433
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor  # noqa: WPS433
    from opentelemetry.instrumentation.logging import LoggingInstrumentor  # noqa: WPS433
    from opentelemetry.sdk.resources import SERVICE_NAME, Resource  # noqa: WPS433
    from opentelemetry.sdk.trace import TracerProvider  # noqa: WPS433
    from opentelemetry.sdk.trace.export import BatchSpanProcessor  # noqa: WPS433

    OPTIONAL_DEPS_NOT_INSTALLED = False
except ImportError:
    OPTIONAL_DEPS_NOT_INSTALLED = True
    logger.warning(
        "Unable to import packages for instrumentation. Ensure you have installed emma-common with the `production` group."
    )


def setup_tracing(service_name: str, otlp_endpoint: str) -> None:
    """Setup tracing for the API.

    This will only work providing the relevant packages are installed.
    """
    if OPTIONAL_DEPS_NOT_INSTALLED:
        logger.warning("Production deps not installed. Returning without doing anything.")
        return

    resource = Resource.create(attributes={SERVICE_NAME: service_name})
    exporter = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)


def instrument_fastapi_app(app: FastAPI) -> None:
    """Instrument the FastAPI app.

    This will only work providing the relevant packages are installed.
    """
    if OPTIONAL_DEPS_NOT_INSTALLED:
        logger.warning("Production deps not installed. Returning without doing anything.")
        return

    LoggingInstrumentor().instrument()
    HTTPXClientInstrumentor().instrument()
    BotocoreInstrumentor().instrument()
    FastAPIInstrumentor.instrument_app(app)


def get_tracer() -> trace.Tracer | None:
    """Get the tracer to use with tracing."""
    if OPTIONAL_DEPS_NOT_INSTALLED:
        logger.warning("Production deps not installed. Unable to get the tracer.")
        return None

    return trace.get_tracer(__name__)
