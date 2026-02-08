from enum import Enum


class EnergyUnit(Enum):
    WATT = "W"
    JOULE = "J"


class UnitPrefix(Enum):
    AUTO = None  # let the function figure it out
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

