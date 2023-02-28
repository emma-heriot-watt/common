from loguru import logger
from watchtower import CloudWatchLogHandler


def add_cloudwatch_handler_to_logger(
    boto3_profile_name: str,
    log_stream_name: str,
    log_group_name: str,
    send_interval: int = 1,
    *,
    enable_trace_logging: bool = False,
) -> None:
    """Add the AWS CloudWatch logger handler to send application logs to CloudWatch."""
    log_handler = CloudWatchLogHandler(
        boto3_profile_name=boto3_profile_name,
        log_stream_name=log_stream_name,
        log_group_name=log_group_name,
        send_interval=send_interval,
    )
    log_handler.formatter.add_log_record_attrs = [  # type: ignore[union-attr]
        "levelname",
        "funcName",
        "lineno",
        "process",
    ]

    if enable_trace_logging:
        log_handler.formatter.add_log_record_attrs.extend(  # type: ignore[union-attr]
            ["otelSpanID", "otelTraceID"]
        )

    logger.add(log_handler, format="{message} | {extra}")
