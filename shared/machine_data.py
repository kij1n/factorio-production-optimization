from dataclasses import dataclass
from .quality import Quality
from .module import Module

@dataclass
class MachineData:
    quality: Quality
    speed: float
    modules: list[Module]
    beacons: int
    beacon_quality: Quality
    level: int = 1  # only applicable to assemblers, available: 1, 2, 3

class MachineName:
    ASM = "assembler"
    CH_PLANT = "chemical_plant"
    REFINERY = "oil_refinery"