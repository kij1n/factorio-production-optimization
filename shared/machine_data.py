from dataclasses import dataclass
from .module import Module

class MachineName:
    ASM = "assembler"
    CH_PLANT = "chemical_plant"
    REFINERY = "oil_refinery"

@dataclass
class MachineData:
    name: MachineName
    speed: float
    modules: list[Module]
    level: int = 1  # only applicable to assemblers, available: 1, 2, 3
