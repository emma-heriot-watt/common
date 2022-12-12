from loguru import logger


try:
    from watchtower import CloudWatchLogHandler

    OPTIONAL_DEPS_NOT_INSTALLED = False
except ImportError:
    OPTIONAL_DEPS_NOT_INSTALLED = True
    logger.warning(
        "Watchtower package not found. Ensure you have installed emma-common with the `aws` group."
    )


def add_cloudwatch_handler_to_logger(
    boto3_profile_name: str, log_stream_name: str, log_group_name: str, send_interval: int = 1
) -> None:
    """Add the AWS CloudWatch logger handler to send application logs to CloudWatch."""
    if OPTIONAL_DEPS_NOT_INSTALLED:
        logger.warning("AWS deps not installed. Returning without doing anything.")
        return

    log_handler = CloudWatchLogHandler(
        boto3_profile_name=boto3_profile_name,
        log_stream_name=log_stream_name,
        log_group_name=log_group_name,
        send_interval=send_interval,
    )
    log_handler.formatter.add_log_record_attrs = [  # pyright: ignore
        "levelname",
        "funcName",
        "lineno",
        "process",
    ]
    logger.add(log_handler, format="{message} | {extra}")
