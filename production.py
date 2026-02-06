from shared import Recipe, Machine


class Production:
    def __init__(self, recipe: Recipe, machine: Machine):
        self.augmented_recipe = self._calc_recipe_values(recipe)
        self.recipe = recipe
        self.machine = machine

    def _calc_recipe_values(self, recipe) -> Recipe:
        aug_recipe = recipe
        prod = recipe.base_prod + self.machine.get_prod()

    def get_machines_qty(self) -> int:
        pass

    def get_recipe_array(items: set[Item]) -> list[Int]:
        pass
