from beacon import Beacon
from shared import ModuleName
from shared.machine_data import *


class Machine:
    """
    A class dedicated to hold information about a single machine.
    Its modules, beacons, speed, quality, etc.
    """

    def __init__(self,data: MachineData, module_data: dict, beacons: tuple[Beacon, int]):
        self.data = data
        self.module_data = module_data
        self.beacons = beacons

    def get_speed(self):
        # calculate speed based on modules, beacons, etc.
        pass

    def get_prod(self):
        prod = 0
        for module in self.data.modules:
            if module.name == ModuleName.PRODUCTIVITY:
                prod += self.module_data[module.name][module.level]
        return prod
