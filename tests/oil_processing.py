from recipes import *
import numpy as np


def get_amounts_used(recipe):
    """
    Get the amount each recipe uses
    :param recipe: Recipe object
    :return: array of amounts (heavy_oil, light_oil, gas)
    A positive number indicates the recipe produces that resource
    """
    input_values = recipe.input_values
    output_values = recipe.output_values
    amounts = [
        output_values.get(Item.HEAVY_OIL, 0) - input_values.get(Item.HEAVY_OIL, 0),
        output_values.get(Item.LIGHT_OIL, 0) - input_values.get(Item.LIGHT_OIL, 0),
        output_values.get(Item.PETROLEUM_GAS, 0)
        - input_values.get(Item.PETROLEUM_GAS, 0),
    ]
    return amounts


def oil_processing(heavy_oil, light_oil, gas):
    """
    :param heavy_oil: amount of heavy oil to be produced
    :param light_oil: amount of light oil to be produced
    :param gas: amount of petroleum gas to be produced
    :return: tuple of how many machines are needed
    (heavy_oil_machines, light_oil_machines, gas_machines)
    """
    recipes = (
        Recipes.recipes[RecipeName.HEAVY_OIL_CRACKING],
        Recipes.recipes[RecipeName.LIGHT_OIL_CRACKING],
        Recipes.recipes[RecipeName.ADVANCED_OIL_PROCESSING],
    )
    recipe_amounts = np.array(
        [
            # heavy oil produced, light oil produced, gas produced
            get_amounts_used(recipes[0]),
            get_amounts_used(recipes[1]),
            get_amounts_used(recipes[2]),
        ]
    ).transpose()
    target_amounts = np.array([heavy_oil, light_oil, gas])
    recipe_amounts = np.linalg.solve(recipe_amounts, target_amounts)

    machines = [None, None, None]
    for i, recipe in enumerate(recipes):
        amount = recipe_amounts[i]
        machines[i] = recipe.get_machines(amount)

    return machines
