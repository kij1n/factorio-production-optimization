import numpy as np

from items import Item

class RecipeName:
    ADVANCED_OIL_PROCESSING = "advanced-oil-processing"
    HEAVY_OIL_CRACKING = "heavy-oil-cracking"
    LIGHT_OIL_CRACKING = "light-oil-cracking"

class Recipe:
    def __init__(self, input_values: dict, output_values: dict, time):
        self.input_values = input_values
        self.output_values = output_values
        self.time = time

    def get_machines(self, recipes_per_second: float) -> int:
        return int(np.ceil(self.time * recipes_per_second))

class Recipes:
    recipes = {
        RecipeName.ADVANCED_OIL_PROCESSING: Recipe(
            {Item.WATER: 50, Item.CRUDE_OIL: 100},
            {Item.HEAVY_OIL: 25, Item.LIGHT_OIL: 45, Item.PETROLEUM_GAS: 55},
            5
        ),
        RecipeName.HEAVY_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.HEAVY_OIL: 40},
            {Item.LIGHT_OIL: 30},
            2
        ),
        RecipeName.LIGHT_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.LIGHT_OIL: 30},
            {Item.PETROLEUM_GAS: 20},
            2
        )
    }
