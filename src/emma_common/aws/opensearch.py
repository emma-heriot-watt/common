from loguru import logger


try:
    from opensearch_logger import OpenSearchHandler

    OPTIONAL_DEPS_NOT_INSTALLED = False
except ImportError:
    OPTIONAL_DEPS_NOT_INSTALLED = True
    logger.warning(
        "OpenSearch packages not found. Ensure you have installed emma-common with the `aws` group."
    )


def add_opensearch_handler_to_logger(
    username: str,
    password: str,
    index_name: str,
    host: str,
    flush_frequency: int = 1,
) -> None:
    """Add the OpenSearch logger handler to send application logs to OpenSearch."""
    if OPTIONAL_DEPS_NOT_INSTALLED:
        logger.warning("AWS deps not installed. Returning without doing anything.")
        return
    log_handler = OpenSearchHandler(
        index_name=index_name,
        hosts=[host],
        flush_frequency=flush_frequency,
        http_auth=(username, password),
        http_compress=True,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
    logger.add(log_handler, format="{message}")
