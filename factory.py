from production import Production
from shared import Item, Recipe, MachineName, RecipeName
import numpy as np
from machine import Machine

class Factory:
    def __init__(
        self,
        outputs: dict[Item, float],
        inputs: list[Item],
        machines: dict[MachineName, Machine],
        available_recipes: list[Recipe],
        forced_recipes: list[Recipe] = None,
    ):
        self.outputs = outputs
        self.inputs = inputs
        self.machines = machines
        self.forced_recipes = forced_recipes

        self.used_recipes = self._find_recipes(available_recipes)
        self.used_items = self._find_items()
        self.productions = self._create_production_instances()

        self.master_matrix = None
        self.solution_vector = None
        self.recipe_count = None

    def _create_production_instances(self) -> list[Production]:
        productions = []
        for recipe in self.used_recipes:
            production = Production(recipe, self.machines.get(recipe.machine_name, None))
            productions.append(production)
        return productions

    def _find_recipes(self, available_recipes) -> list[Recipe]:
        recipes = []
        for output in self.outputs.keys():
            for recipe in self.forced_recipes:
                if output in recipe.output_values.keys():
                    recipes.append(recipe)
                    break
            for recipe in available_recipes.values():
                if output in recipe.output_values.keys():
                    if recipe in recipes:
                        continue
                    recipes.append(recipe)
                    break
        for input_resource in self.inputs:
            recipe = Recipe({}, {input_resource: 1}, 1, None, RecipeName.NO_RECIPE)
            recipes.append(recipe)
        return recipes

    def _find_items(self) -> set[Item]:
        items = set()
        for recipe in self.used_recipes:
            for item in recipe.input_values.keys():
                items.add(item)
            for item in recipe.output_values.keys():
                items.add(item)
        return items

    def create_master_matrix(self):
        arrays = []
        for production in self.productions:
            recipe_array = production.get_recipe_array(self.used_items)
            arrays.append(recipe_array)

        master_matrix = np.array([*arrays]).transpose()
        solution_array = []
        for item in sorted(self.used_items):
            solution_array.append(self.outputs.get(item, 0))

        solution_vector = np.array(solution_array)

        self.master_matrix = master_matrix
        self.solution_vector = solution_vector

    def find_solution(self):
        solution_array = np.linalg.solve(self.master_matrix, self.solution_vector)
        self.recipe_count = solution_array

    def get_machine_count(self) -> dict[Recipe, int]:
        machines = {}
        for i, production in enumerate(self.productions):
            machines[production.augmented_recipe] = production.get_machines_qty(
                self.recipe_count[i]
            )
        return machines
