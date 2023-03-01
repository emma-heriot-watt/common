import io
from typing import Any

import torch


class TorchDataMixin:
    """A utility class containing useful functions for torch serialisation."""

    @staticmethod
    def to_bytes(  # noqa: WPS602
        raw_object: Any,
    ) -> bytes:
        """Factory method that builds a byte representation from a raw object."""
        buffer = io.BytesIO()
        torch.save(raw_object, buffer)

        buffer.seek(0)

        return buffer.read()

    @staticmethod
    def get_object(object_bytes: bytes) -> Any:  # noqa: WPS602
        """Loads the object from the byte representation contained in the response body."""
        buffer = io.BytesIO(object_bytes)

        return torch.load(buffer)
