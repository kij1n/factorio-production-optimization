from shared import ModuleName
from shared.machine_data import *

class Machine:
    """
    A class dedicated to hold information about a single machine.
    Its modules, beacons, speed, quality, etc.
    """
    def __init__(self, name: MachineName, data: MachineData, module_data: dict):
        self.name = name
        self.data = data
        self.module_data = module_data

    def get_speed(self):
        # calculate speed based on modules, beacons, etc.
        pass

    def get_prod(self):
        prod = 0
        for module in self.data.modules:
            if module.name == ModuleName.PRODUCTIVITY:
                prod += self.module_data[module.name][module.level]

