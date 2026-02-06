from shared import MachineName


class RecipeName:
    NO_RECIPE = None
    ADVANCED_OIL_PROCESSING = "advanced-oil-processing"
    HEAVY_OIL_CRACKING = "heavy-oil-cracking"
    LIGHT_OIL_CRACKING = "light-oil-cracking"


class Recipe:
    def __init__(
        self,
        input_values: dict,
        output_values: dict,
        time,
        machine_name: MachineName,
        recipe_name: RecipeName,
        base_productivity: float = 100,
    ):
        self.input_values = input_values
        self.output_values = output_values
        self.time = time
        self.machine_name = machine_name
        self.recipe_name = recipe_name
        self.base_prod = base_productivity / 100
