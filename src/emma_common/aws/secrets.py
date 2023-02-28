from typing import TYPE_CHECKING

from boto3.session import Session


if TYPE_CHECKING:
    from mypy_boto3_secretsmanager.client import SecretsManagerClient
    from mypy_boto3_secretsmanager.type_defs import GetSecretValueResponseTypeDef


def retrieve_secret(
    profile_name: str, secret_name: str, region_name: str
) -> GetSecretValueResponseTypeDef:
    """Retrieve secrets from the AWS Secrets Manager."""
    client: SecretsManagerClient = Session(profile_name=profile_name).client(
        service_name="secretsmanager", region_name=region_name
    )
    return client.get_secret_value(SecretId=secret_name)
