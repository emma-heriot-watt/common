import torch

from emma_common.datamodels import EmmaExtractedFeatures
from emma_common.datamodels.torch import TorchDataMixin


def test_emma_extracted_features_parses_correctly() -> None:
    features = EmmaExtractedFeatures(
        bbox_features=torch.randn(3, 10),
        bbox_coords=torch.randn(3, 10),
        bbox_probas=torch.randn(3, 10),
        cnn_features=torch.randn(3, 10),
        class_labels=["label1", "label2"],
        width=100,
        height=300,
    )

    assert features


def test_emma_extracted_features_converts_to_json_properly() -> None:
    features = EmmaExtractedFeatures(
        bbox_features=torch.randn(3, 10),
        bbox_coords=torch.randn(3, 10),
        bbox_probas=torch.randn(3, 10),
        cnn_features=torch.randn(3, 10),
        class_labels=["label1", "label2"],
        width=100,
        height=300,
    )

    assert features

    bytes_features = TorchDataMixin.to_bytes(features)

    parsed_features = TorchDataMixin.get_object(bytes_features)

    assert isinstance(parsed_features, EmmaExtractedFeatures)
