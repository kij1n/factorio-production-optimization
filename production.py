from shared import Recipe, Item
import numpy as np
from machine import Machine


class Production:
    def __init__(self, recipe: Recipe, machine: Machine):
        self.machine = machine
        self.augmented_recipe = self._calc_recipe_values(recipe)
        self.machines_qty = None

    def _calc_recipe_values(self, recipe) -> Recipe:
        if self.machine is None:
            return recipe

        aug_recipe = recipe
        prod = recipe.base_prod + self.machine.get_prod()
        aug_recipe.output_values = {
            key: value * prod for key, value in aug_recipe.output_values.items()
        }
        return aug_recipe

    def get_machines_qty(self, recipes_per_sec: float) -> int:
        if self.machines_qty is not None:
            return self.machines_qty

        speed = self.machine.get_speed() if self.machine is not None else 1

        return int(np.ceil(recipes_per_sec * self.augmented_recipe.time / speed))

    def get_recipe_array(self, items: set[Item]) -> list[int]:
        """
        Input values are negative, output positive.
        :param items: A set of items that factory uses, later sorted.
        :return: A sorted list with values for each item
        """
        recipe_array = []
        input_values = self.augmented_recipe.input_values
        output_values = self.augmented_recipe.output_values

        for item in sorted(items):
            value = 0
            if item in input_values.keys():
                value -= input_values[item]
            if item in output_values.keys():
                value += output_values[item]
            recipe_array.append(value)

        return recipe_array
