import json
from contextlib import suppress
from functools import cache
from pathlib import Path
from typing import TYPE_CHECKING, Any

from opentelemetry.semconv.resource import ResourceAttributes


if TYPE_CHECKING:
    from opentelemetry.sdk.resources import Attributes


@cache
def load_ec2_instance_metadata() -> dict[str, Any]:
    """Try to load the metadata for the current EC2 instance.

    This will raise an FileNotFoundError if the file does not exist, which will happen if we are
    not running on an Ubuntu-based EC2 instance.
    """
    metadata_file = Path("/run/cloud-init/instance-data.json")
    if not metadata_file.exists():
        raise FileNotFoundError("Metadata does not exist.")

    return json.loads(metadata_file.read_text())


def create_resource_attributes() -> Attributes:
    """Create attributes dict for the resource.

    We try to fill in as many attributes as possible, ignoring those that are not available.
    """
    try:
        metadata = load_ec2_instance_metadata()
        instance_metadata = metadata["v1"]
    except FileNotFoundError:
        return {}

    attributes: Attributes = {}
    attributes[ResourceAttributes.OS_TYPE] = "linux"

    with suppress(KeyError):
        attributes[ResourceAttributes.SERVICE_INSTANCE_ID] = instance_metadata["instance_id"]
        attributes[ResourceAttributes.HOST_ID] = instance_metadata["instance_id"]

    with suppress(KeyError):
        attributes[ResourceAttributes.CLOUD_PROVIDER] = instance_metadata["cloud_name"]

    with suppress(KeyError):
        attributes[ResourceAttributes.CLOUD_AVAILABILITY_ZONE] = instance_metadata[
            "availability_zone"
        ]

    with suppress(KeyError):
        attributes[ResourceAttributes.CLOUD_REGION] = instance_metadata["region"]

    with suppress(KeyError):
        attributes[
            ResourceAttributes.CLOUD_PLATFORM
        ] = f"{instance_metadata['cloud_name']}_{instance_metadata['platform']}"

    with suppress(KeyError):
        attributes[ResourceAttributes.HOST_NAME] = instance_metadata["host_name"]

    with suppress(KeyError):
        attributes[ResourceAttributes.HOST_TYPE] = metadata["meta-data"]["instance-type"]

    with suppress(KeyError):
        attributes[ResourceAttributes.HOST_ARCH] = instance_metadata["machine"].split("_")[0]

    with suppress(KeyError):
        attributes[ResourceAttributes.HOST_IMAGE_ID] = metadata["meta-data"]["ami-id"]

    with suppress(KeyError):
        attributes[ResourceAttributes.OS_DESCRIPTION] = instance_metadata["system_platform"]

    with suppress(KeyError):
        attributes[ResourceAttributes.OS_NAME] = instance_metadata["variant"]

    with suppress(KeyError):
        attributes[ResourceAttributes.OS_VERSION] = instance_metadata["distro_version"]

    return attributes
