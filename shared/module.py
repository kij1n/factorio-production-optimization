from dataclasses import dataclass
from enum import Enum

from shared import Quality


class ModuleName(Enum):
    SPEED = "speed"
    PRODUCTIVITY = "productivity"
    EFFICIENCY = "efficiency"


@dataclass
class ModuleData:
    level: int  # 1-3
    quality: Quality


class Module:
    def __init__(self, name: ModuleName, data: ModuleData):
        self.name = name
        self.level = data.level
        self.quality = data.quality
