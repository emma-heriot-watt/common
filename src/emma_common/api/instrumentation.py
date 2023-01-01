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
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_NAMESPACE, SERVICE_VERSION, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from emma_common.aws.ec2 import create_resource_attributes


def create_resource(service_name: str, service_version: str, service_namespace: str) -> Resource:
    """Create Resource for OTEL."""
    # Prepare the resource attributes
    resource_attributes = create_resource_attributes()
    resource_attributes[SERVICE_NAME] = service_name
    resource_attributes[SERVICE_VERSION] = service_version
    resource_attributes[SERVICE_NAMESPACE] = service_namespace

    # Create the resource
    resource = Resource.create(attributes=resource_attributes)
    return resource


def setup_tracing(otlp_endpoint: str, resource: Resource) -> None:
    """Setup tracing for the API."""
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


def instrument_app(
    app: FastAPI,
    *,
    otlp_endpoint: str,
    service_name: str,
    service_version: str,
    service_namespace: str,
) -> None:
    """Instrument the API."""
    resource = create_resource(
        service_name=service_name,
        service_version=service_version,
        service_namespace=service_namespace,
    )
    setup_tracing(otlp_endpoint=otlp_endpoint, resource=resource)
    run_instrumentation(app)

    logger.info("Application instrumented successfully.")
