from __future__ import annotations

from typing import TYPE_CHECKING, Any

from fastapi import BackgroundTasks, Response

from emma_common.datamodels.torch import TorchDataMixin


if TYPE_CHECKING:
    from collections.abc import Mapping


class TorchResponse(Response):
    """HTTP response containing arbitrary bytes that are serialised using Torch.pickle format.

    For more information about the protocol: https://pytorch.org/docs/stable/generated/torch.save.html#torch-save
    """

    def __init__(
        self,
        raw_object: Any,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
        background: BackgroundTasks | None = None,
    ) -> None:
        """Creates a new response object that contains pickled data."""
        media_type = "application/octet-stream"
        raw_content = TorchDataMixin.to_bytes(raw_object)
        super().__init__(raw_content, status_code, headers, media_type, background)
