from beacon import Beacon
from shared import ModuleName
from shared.machine_data import *
import numpy as np


class Machine:
    """
    A class dedicated to hold information about a single machine.
    Its modules, beacons, speed, quality, etc.
    Attributes:
        data (MachineData): contains basic information about a machine
        module_data (dict): contains information about moduls used by a maschine
        beacons (tuple[Beacon, int]): information about beacons affecting this machine
        speed (float): calculated speed of a machine
        prod (float): producitivity multiplier
        eff (float): power usage multiplier, inclused penalty from productivity modules
    """

    def __init__(
        self, data: MachineData, module_data: dict, beacons: tuple[Beacon, int]
    ):
        self.data = data
        self.module_data = module_data
        self.beacons = beacons

        self.speed = self._get_bonus(ModuleName.SPEED)
        self.prod = self._get_bonus(ModuleName.PRODUCTIVITY)
        self.eff = self._get_bonus(ModuleName.EFFICIENCY)

    def _get_bonus(self, name: ModuleName):
        multiplier = 1
        multiplier += self._get_bonus_modules(name)
        multiplier += self._get_bonus_beacons(name)

        return max(multiplier, 0.2) * self._mul_by_speed(name)

    def _mul_by_speed(self, name: ModuleName):
        if name == ModuleName.SPEED:
            return self.data.speed
        return 1

    def _get_bonus_modules(self, name: ModuleName):
        bonus = 0
        for module in self.data.modules:
            if name == ModuleName.SPEED:
                bonus += self._get_bonus_if(module, name)
                bonus -= self._get_bonus_if(
                    module, ModuleName.PRODUCTIVITY, "speed_decrease"
                )
            elif name == ModuleName.EFFICIENCY:
                bonus -= self._get_bonus_if(module, name)
                bonus -= self._get_bonus_if(
                    module, ModuleName.PRODUCTIVITY, "energy_consumption"
                )
                bonus -= self._get_bonus_if(
                    module, ModuleName.SPEED, "energy_consumption"
                )

            elif name == ModuleName.PRODUCTIVITY:
                bonus += self._get_bonus_if(module, name)

        return bonus

    def _get_bonus_beacons(self, name: ModuleName):
        if name == ModuleName.PRODUCTIVITY or self.beacons[0].modules is None:
            return 0

        bonus = 0
        for module in self.beacons[0].modules:
            bonus += self._get_bonus_if(module, name)
        return bonus * self._get_comb_trans_str(*self.beacons)

    def _get_bonus_if(self, module: Module, name: ModuleName, special: str = ""):
        if module.name == name:
            return self.module_data[module.name.value][str(module.level)][
                str(module.quality.value) if special == "" else special
            ]
        return 0

    @staticmethod
    def _get_comb_trans_str(beacon, n):
        return beacon.efficiency * np.sqrt(n)

    def get_prod(self):
        return self.prod

    def get_speed(self):
        return self.speed

    def get_eff(self):
        return self.eff
