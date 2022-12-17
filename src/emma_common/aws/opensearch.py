from loguru import logger
from opensearch_logger import OpenSearchHandler


def add_opensearch_handler_to_logger(
    username: str,
    password: str,
    index_name: str,
    host: str,
    flush_frequency: int = 1,
) -> None:
    """Add the OpenSearch logger handler to send application logs to OpenSearch."""
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
