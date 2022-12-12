from __future__ import annotations

from loguru import logger


try:  # noqa: WPS229
    from boto3.session import Session
    from mypy_boto3_secretsmanager.client import SecretsManagerClient
    from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef

    OPTIONAL_DEPS_NOT_INSTALLED = False
except ImportError:
    OPTIONAL_DEPS_NOT_INSTALLED = True
    logger.warning(
        "Boto3 package not found. Ensure you have installed emma-common with the `aws` group."
    )


def retrieve_secret(
    profile_name: str, secret_name: str, region_name: str
) -> GetSecretValueResponseTypeDef:
    """Retrieve secrets from the AWS Secrets Manager."""
    client: SecretsManagerClient = Session(profile_name=profile_name).client(
        service_name="secretsmanager", region_name=region_name
    )
    return client.get_secret_value(SecretId=secret_name)
