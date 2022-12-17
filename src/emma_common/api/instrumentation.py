"""Easily instrument and handle tracing for the application.

This module makes handling instrumentation for observability much easier. This will only work
providing the relevant packages are installed. If they're not installed, the various functions will
do nothing.
"""

from fastapi import FastAPI
from loguru import logger
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.botocore import BotocoreInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def setup_tracing(service_name: str, otlp_endpoint: str) -> None:
    """Setup tracing for the API."""
    resource = Resource.create(attributes={SERVICE_NAME: service_name})
    exporter = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)


def run_instrumentation(app: FastAPI) -> None:
    """Instrument everything possible."""
    LoggingInstrumentor().instrument()
    HTTPXClientInstrumentor().instrument()
    BotocoreInstrumentor().instrument()
    FastAPIInstrumentor.instrument_app(app)


def instrument_app(app: FastAPI, service_name: str, otlp_endpoint: str) -> None:
    setup_tracing(service_name=service_name, otlp_endpoint=otlp_endpoint)
    run_instrumentation(app)

    logger.info("Application instrumented successfully.")
