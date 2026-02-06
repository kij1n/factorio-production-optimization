from dataclasses import dataclass
from shared import Module


@dataclass
class Beacon:
    efficiency: float = None
    modules: list[Module] = None
