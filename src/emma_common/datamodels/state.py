from enum import Enum
from typing import Optional

from pydantic import BaseModel

from emma_common.datamodels import EmmaExtractedFeatures


class SpeakerRole(Enum):
    """Speaker roles."""

    user = "user"
    agent = "agent"


class DialogueUtterance(BaseModel, frozen=True):
    """Single utterance model for the Emma Policy client."""

    utterance: str
    role: SpeakerRole


class EnvironmentStateTurn(BaseModel):
    """State of the environment at a single timestep."""

    features: list[EmmaExtractedFeatures]
    output: Optional[str] = None


class EmmaPolicyRequest(BaseModel):
    """Request model for the Emma Policy client."""

    dialogue_history: list[DialogueUtterance]
    environment_history: list[EnvironmentStateTurn]
    force_stop_token: bool = False
    inventory: Optional[str] = None
    entity_label: Optional[str] = None

    @property
    def num_images(self) -> int:
        """Get the number of images being send to the model."""
        return sum([len(turn.features) for turn in self.environment_history])
