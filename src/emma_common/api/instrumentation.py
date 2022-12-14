"""Easily instrument and handle tracing for FastAPI.

This module makes handling instrumentation for observability much easier. This will only work
providing the relevant packages are installed. If they're not installed, the various functions will
do nothing.
"""

from logging import LogRecord
from typing import Any

from fastapi import FastAPI
from loguru import logger

from emma_common.logging import InterceptHandler


try:  # noqa: WPS229
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.instrumentation.botocore import BotocoreInstrumentor
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
    from opentelemetry.instrumentation.logging import LoggingInstrumentor
    from opentelemetry.sdk.resources import SERVICE_NAME, Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    OPTIONAL_DEPS_NOT_INSTALLED = False
except ImportError:
    OPTIONAL_DEPS_NOT_INSTALLED = True
    logger.warning(
        "Unable to import packages for instrumentation. Ensure you have installed emma-common with the `api` group."
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


class InstrumentedInterceptHandler(InterceptHandler):
    """Customised version of the InterceptHandler for the instrumented API."""

    def _bind(self, record: LogRecord) -> dict[str, Any]:
        """Add span and trace information to the log.

        After being instrumented, this information is available to the application.
        """
        try:
            return {
                "otelSpanID": record.otelSpanID,  # type: ignore[attr-defined]
                "otelTraceID": record.otelTraceID,  # type: ignore[attr-defined]
            }
        except Exception:
            return {}
