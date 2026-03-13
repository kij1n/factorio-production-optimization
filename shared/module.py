from enum import Enum

from shared import Quality


class ModuleName(Enum):
    SPEED = "speed"
    PRODUCTIVITY = "productivity"
    EFFICIENCY = "efficiency"


class Module:
    def __init__(self, name: ModuleName, level: int, quality: Quality):
        self.name = name
        self.level = level
        self.quality = quality
