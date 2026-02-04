from .machine_data import *

class Machine:
    """
    A class dedicated to hold information about a single machine.
    Its modules, beacons, speed, quality, etc.
    """
    def __init__(self, name: MachineName, data: MachineData):
        self.name = name
        self.data = data

    def get_speed(self):
        # calculate speed based on modules, beacons, etc.
        pass