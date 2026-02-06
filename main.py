from shared import *
import json_loader


def get_recipes():
    recipes = {
        RecipeName.ADVANCED_OIL_PROCESSING: Recipe(
            {Item.WATER: 50, Item.CRUDE_OIL: 100},
            {Item.HEAVY_OIL: 25, Item.LIGHT_OIL: 45, Item.PETROLEUM_GAS: 55},
            5,
            MachineName.REFINERY,
        ),
        RecipeName.HEAVY_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.HEAVY_OIL: 40},
            {Item.LIGHT_OIL: 30},
            2,
            MachineName.CH_PLANT,
        ),
        RecipeName.LIGHT_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.LIGHT_OIL: 30},
            {Item.PETROLEUM_GAS: 20},
            2,
            MachineName.CH_PLANT,
        ),
    }
    return recipes


def prepare_machines():
    pass


def main():
    available_recipes = get_recipes()
    constants = json_loader.load_const()
