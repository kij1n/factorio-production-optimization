from production import Production
from shared import Machine, Item, Recipe, MachineName


class Factory:
    def __init__(
            self, outputs: dict[Item, float], inputs: list[Item],
            machines: dict[MachineName, Machine], forced_recipes: list[Recipe],
            available_recipes: list[Recipe]
    ):
        self.outputs = outputs
        self.inputs = inputs
        self.machines = machines
        self.forced_recipes = forced_recipes

        self.used_recipes = self._find_recipes(available_recipes)
        self.used_items = self._find_items()
        self.productions = self._create_production_instances()

    def _create_production_instances(self) -> list[Production]:
        productions = []
        for recipe in self.used_recipes:
            production = Production(
                recipe, self.machines[recipe.machine_name]
            )
            productions.append(production)
        return productions

    def _find_recipes(self, available_recipes) -> list[Recipe]:
        recipes = []
        for output in self.outputs.keys():
            for recipe in self.forced_recipes:
                if output in recipe.output_values.keys():
                    recipes.append(recipe)
                    continue
            for recipe in available_recipes:
                if output in recipe.output_values.keys():
                    recipes.append(recipe)
        for input_resource in self.inputs:
            recipe = Recipe(
                {},
                {input_resource: 1},
                1, None
            )
            recipes.append(recipe)
        return recipes

    def _find_items(self) -> set[Item]:
        items = set()
        for recipe in self.used_recipes:
            items.add(recipe.input_values.keys())
        return items