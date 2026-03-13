from enum import Enum
import numpy as np


class EnergyUnit(Enum):
    WATT = "W"
    JOULE = "J"


class UnitPrefix(Enum):
    NANO = (-9, "n")
    MICRO = (-6, "u")
    MILI = (-3, "m")
    NONE = (0, "")
    KILO = (3, "k")
    MEGA = (6, "M")
    GIGA = (9, "G")
    TERA = (12, "T")
    PETA = (15, "P")


class TimeUnit(Enum):
    MILISECOND = 0.001
    SECOND = 1
    MINUTE = 60
    HOUR = 3600
    DAY = 3600 * 24


def find_unit(order: int) -> UnitPrefix:
    exponent = 3 * np.floor(order / 3)

    if exponent < UnitPrefix[0].value[0]:
        return UnitPrefix[0]
    elif exponent > UnitPrefix[-1].value[0]:
        return UnitPrefix[-1]

    for prefix in list(UnitPrefix)[1:-1]:
        if exponent == prefix.value[0]:
            return prefix

    return UnitPrefix.NONE
