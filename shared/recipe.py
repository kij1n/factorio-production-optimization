from items import Item
from shared import MachineName


class RecipeName:
    ADVANCED_OIL_PROCESSING = "advanced-oil-processing"
    HEAVY_OIL_CRACKING = "heavy-oil-cracking"
    LIGHT_OIL_CRACKING = "light-oil-cracking"

class Recipe:
    def __init__(
            self, input_values: dict, output_values: dict,
            time, machine_name: MachineName, base_productivity: float = 100
    ):
        self.input_values = input_values
        self.output_values = output_values
        self.time = time
        self.machine_name = machine_name
        self.base_prod = base_productivity / 100

class Recipes:
    recipes = {
        RecipeName.ADVANCED_OIL_PROCESSING: Recipe(
            {Item.WATER: 50, Item.CRUDE_OIL: 100},
            {Item.HEAVY_OIL: 25, Item.LIGHT_OIL: 45, Item.PETROLEUM_GAS: 55},
            5, MachineName.REFINERY
        ),
        RecipeName.HEAVY_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.HEAVY_OIL: 40},
            {Item.LIGHT_OIL: 30},
            2, MachineName.CH_PLANT
        ),
        RecipeName.LIGHT_OIL_CRACKING: Recipe(
            {Item.WATER: 30, Item.LIGHT_OIL: 30},
            {Item.PETROLEUM_GAS: 20},
            2, MachineName.CH_PLANT
        )
    }
