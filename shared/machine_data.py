from dataclasses import dataclass
from .quality import Quality
from .module import Module

@dataclass
class MachineData:
    quality: Quality
    speed: float
    modules: list[Module]
    module_quality: Quality
    beacons: int
    beacon_quality: Quality
    level: int = 0  # only applicable to assemblers

class MachineName:
    ASM = "assembler"
    CH_PLANT = "chemical_plant"
    REFINERY = "oil_refinery"