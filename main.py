from beacon import Beacon
from factory import Factory
from shared import *
import json_loader


def get_recipes():
    recipes = {
        RecipeName.ADVANCED_OIL_PROCESSING: Recipe(
            {Item.WATER: 50, Item.CRUDE_OIL: 100},
            {Item.HEAVY_OIL: 25, Item.LIGHT_OIL: 45, Item.PETROLEUM_GAS: 55},
            5,
            MachineName.REFINERY,
            RecipeName.ADVANCED_OIL_PROCESSING,
        ),
        RecipeName.HEAVY_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.HEAVY_OIL: 40},
            {Item.LIGHT_OIL: 30},
            2,
            MachineName.CH_PLANT,
            RecipeName.HEAVY_OIL_CRACKING,
        ),
        RecipeName.LIGHT_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.LIGHT_OIL: 30},
            {Item.PETROLEUM_GAS: 20},
            2,
            MachineName.CH_PLANT,
            RecipeName.LIGHT_OIL_CRACKING,
        ),
    }
    return recipes


def prepare_machines(constants: dict):
    asm_level = 1
    asm_quality = Quality.NORMAL
    asm_data = MachineData(
        constants[MachineName.ASM][asm_level][asm_quality.value], [], asm_level
    )
    asm_beacons = (Beacon(), 0)

    chm_quality = Quality.NORMAL
    chm_data = MachineData(constants[MachineName.CH_PLANT][chm_quality.value], [])
    chm_beacons = (Beacon(), 0)

    refinery_quality = Quality.NORMAL
    refinery_data = MachineData(
        constants[MachineName.REFINERY][refinery_quality.value], []
    )
    refinery_beacons = (Beacon(), 0)

    machines = {
        MachineName.ASM: Machine(asm_data, constants["modules"], asm_beacons),
        MachineName.CH_PLANT: Machine(chm_data, constants["modules"], chm_beacons),
        MachineName.REFINERY: Machine(
            refinery_data, constants["modules"], refinery_beacons
        ),
    }
    return machines


def print_results(solutions: dict):
    for recipe, machine_count in solutions.items():
        print(f"{recipe.recipe_name}: machine_count ({recipe.machine_name})")


def main():
    available_recipes = get_recipes()
    constants = json_loader.load_const()
    machines = prepare_machines(constants)

    outputs = {Item.HEAVY_OIL: 0, Item.LIGHT_OIL: 0, Item.PETROLEUM_GAS: 100}
    inputs = [Item.WATER, Item.CRUDE_OIL]

    factory = Factory(outputs, inputs, machines, available_recipes, [])

    factory.create_master_matix()
    factory.find_solution()

    solutions = factory.get_machine_count()
    print_results(solutions)
