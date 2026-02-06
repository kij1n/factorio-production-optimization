from shared import Recipe, Machine, Item


class Production:
    def __init__(self, recipe: Recipe, machine: Machine):
        self.augmented_recipe = self._calc_recipe_values(recipe)
        self.recipe = recipe
        self.machine = machine

    def _calc_recipe_values(self, recipe) -> Recipe:
        aug_recipe = recipe.copy()
        prod = recipe.base_prod + self.machine.get_prod()
        aug_recipe.output_values = {
            key: value * prod for key, value in aug_recipe.output_values.items()
        }
        return aug_recipe

    def get_machines_qty(self) -> int:
        pass

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
