from beacon import Beacon
from factory import Factory
from machine import Machine
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


def prepare_refinery_machine(constants) -> Machine:
    refinery_quality = Quality.LEGENDARY
    refinery_modules = [
        Module(ModuleName.PRODUCTIVITY, 3, Quality.LEGENDARY),
        Module(ModuleName.PRODUCTIVITY, 3, Quality.LEGENDARY),
        Module(ModuleName.PRODUCTIVITY, 3, Quality.LEGENDARY)
    ]

    refinery_data = MachineData(
        MachineName.REFINERY, constants["machines"][MachineName.REFINERY][str(refinery_quality.value)], refinery_modules
    )

    beacon_qty = 4
    beacon_quality = Quality.LEGENDARY
    beacon_modules = [
        Module(ModuleName.SPEED, 3, Quality.LEGENDARY),
        Module(ModuleName.SPEED, 3, Quality.LEGENDARY),
    ]

    refinery_beacons = (
        Beacon(constants["beacons"][str(beacon_quality.value)], beacon_modules),
        beacon_qty
    )

    return Machine(refinery_data, constants["modules"], refinery_beacons)


def prepare_chm_machine(constants) -> Machine:
    chm_quality = Quality.LEGENDARY
    chm_modules = [
        Module(ModuleName.PRODUCTIVITY, 3, Quality.LEGENDARY),
        Module(ModuleName.PRODUCTIVITY, 3, Quality.LEGENDARY),
        Module(ModuleName.PRODUCTIVITY, 3, Quality.LEGENDARY)
    ]
    chm_data = MachineData(MachineName.CH_PLANT, constants["machines"][MachineName.CH_PLANT][str(chm_quality.value)], chm_modules)

    beacon_qty = 4
    beacon_quality = Quality.LEGENDARY
    beacon_modules = [
        Module(ModuleName.SPEED, 3, Quality.LEGENDARY),
        Module(ModuleName.SPEED, 3, Quality.LEGENDARY),
    ]

    chm_beacons = (
        Beacon(constants["beacons"][str(beacon_quality.value)], beacon_modules),
        beacon_qty
    )

    return Machine(chm_data, constants["modules"], chm_beacons)


def prepare_asm_machine(constants) -> Machine:
    asm_level = 1
    asm_quality = Quality.LEGENDARY
    asm_data = MachineData(
        MachineName.ASM, constants["machines"][MachineName.ASM][str(asm_level)][str(asm_quality.value)], [], asm_level
    )
    asm_beacons = (Beacon(), 0)
    return Machine(asm_data, constants["modules"], asm_beacons)


def prepare_machines(constants: dict):
    machines = {
        MachineName.ASM: prepare_asm_machine(constants),
        MachineName.CH_PLANT: prepare_chm_machine(constants),
        MachineName.REFINERY: prepare_refinery_machine(constants),
    }
    return machines


def print_results(solutions: dict):
    for recipe, machine_count in solutions.items():
        if recipe.recipe_name == RecipeName.NO_RECIPE:
            continue
        print(f"{recipe.recipe_name} ({recipe.machine_name}): {machine_count}")


def main():
    available_recipes = get_recipes()
    constants = json_loader.load_const()
    machines = prepare_machines(constants)

    outputs = {Item.HEAVY_OIL: 326.25, Item.LIGHT_OIL: 1603.658, Item.PETROLEUM_GAS: 29622.717}
    inputs = [Item.WATER, Item.CRUDE_OIL]

    factory = Factory(outputs, inputs, machines, available_recipes, [])

    factory.create_master_matrix()
    factory.find_solution()

    solutions = factory.get_machine_count()
    print_results(solutions)


if __name__ == "__main__":
    main()
