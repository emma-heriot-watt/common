from typing import Any, Optional

import torch
from pydantic import BaseModel
from typing_extensions import Self


class EmmaExtractedFeatures(BaseModel):
    """Extracted features from an image."""

    bbox_features: torch.Tensor
    bbox_coords: torch.Tensor
    bbox_probas: torch.Tensor
    cnn_features: torch.Tensor
    class_labels: list[str]
    entity_labels: Optional[list[str]] = None
    width: int
    height: int

    class Config:
        """Config for the model class."""

        arbitrary_types_allowed: bool = True

    @classmethod
    def from_raw_response(cls, raw_response: dict[str, Any]) -> Self:
        """Instantiate the features from a raw json response.

        Dict keys that are used below can be found within the emma-simbot/perception repo.
        """
        return cls(
            bbox_features=torch.tensor(raw_response["bbox_features"]),
            bbox_coords=torch.tensor(raw_response["bbox_coords"]),
            bbox_probas=torch.tensor(raw_response["bbox_probas"]),
            cnn_features=torch.tensor(raw_response["cnn_features"]),
            class_labels=raw_response["class_labels"],
            width=raw_response["width"],
            height=raw_response["height"],
            entity_labels=raw_response.get("entity_labels", None),
        )

    @property
    def bbox_areas(self) -> torch.Tensor:
        """Compute the vectorised bbox areas."""
        width = self.bbox_coords[:, 3] - self.bbox_coords[:, 1]
        height = self.bbox_coords[:, 2] - self.bbox_coords[:, 0]
        return width * height
