from beacon import Beacon
from shared import ModuleName
from shared.machine_data import *
import numpy as np


class Machine:
    """
    A class dedicated to hold information about a single machine.
    Its modules, beacons, speed, quality, etc.
    """

    def __init__(
        self, data: MachineData, module_data: dict, beacons: tuple[Beacon, int]
    ):
        self.data = data
        self.module_data = module_data
        self.beacons = beacons

    def get_speed(self):
        # calculate speed based on modules, beacons, etc.
        speed = self.data.speed
        multiplier = 1

        if self.beacons[1] <= 0:
            return speed

        comb_trans_str = self._get_comb_trans_str(*self.beacons)
        multiplier += comb_trans_str * self._get_speed_bonus()
        return speed * multiplier

    def _get_speed_bonus(self):
        bonus = 0
        beacon = self.beacons[0]
        for module in beacon.modules:
            if module.name == ModuleName.SPEED:
                bonus += (
                    self.module_data[module.name.value][str(module.level)][
                        str(module.quality.value)
                    ]
                    / 100
                )
        return bonus

    @staticmethod
    def _get_comb_trans_str(beacon, n):
        return beacon.efficiency * np.sqrt(n)

    def get_prod(self):
        prod = 0
        for module in self.data.modules:
            if module.name == ModuleName.PRODUCTIVITY:
                prod += self.module_data[module.name][module.level]
        return prod
