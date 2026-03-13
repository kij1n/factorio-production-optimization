from production import Production
from shared import *
import numpy as np
from machine import Machine
from functools import cached_property


def _apply_prefix(val: float, prefix: UnitPrefix, unit: EnergyUnit):
    return val * np.power(10, prefix.value[0]), str(prefix.value[1] + unit.value)


def auto_format(func):
    def wrapper(*args, **kwargs):
        power = func(*args, **kwargs)
        output = list(power)
        for val, unit in output:
            prefix = find_prefix(np.log10(power))
            val = apply_prefix(val, prefix)
        return output

    return wrapper


class Factory:
    def __init__(
        self,
        outputs: dict[Item, float],
        inputs: list[Item],
        machines: dict[MachineName, Machine],
        available_recipes: list[Recipe],
        forced_recipes: list[Recipe] = None,
    ):
        self.available_recipes = available_recipes
        self._outputs = outputs
        self._inputs = inputs
        self._machines = machines
        self._forced_recipes = forced_recipes

    def __setattr__(self, name, val):
        if name in [
            "master_matrix",
            "solution",
            "machine_count",
            "total_power",
            "power_per_prod",
        ]:
            raise AttributeError(f"Cannot set read-only attibute: '{name}'")

        if name in ["_outputs", "_inputs", "_machines", "_forced_recipes"]:
            self.__dict__.pop("master_matrix", None)
            self.__dict__.pop("solution", None)
            self.__dict__.pop("machine_count", None)
            self.__dict__.pop("total_power", None)
            self.__dict__.pop("power_per_prod", None)

        super().__setattr__(name, val)

    @property
    def outputs(self):
        return self._outputs

    @property
    def inputs(self):
        return self._inputs

    @property
    def machines(self):
        return self._machines

    @property
    def forced_recipes(self):
        return self._forced_recipes

    @property
    def used_recipes(self):
        return self._find_recipes(self.available_recipes)

    @property
    def used_items(self):
        return self._find_items()

    @cached_property
    def machine_count(self):
        machines = {}
        for i, production in enumerate(self.productions):
            machines[production.augmented_recipe] = production.get_machines_qty(
                self.solution[i]
            )
        return machines

    @cached_property
    def productions(self):
        productions = []
        for recipe in self.used_recipes:
            production = Production(
                recipe, self.machines.get(recipe.machine_name, None)
            )
            productions.append(production)
        return productions

    @cached_property
    def solution(self):
        solution_array = np.linalg.solve(self.master_matrix, self.solution_vector)
        return solution_array

    @cached_property
    def master_matrix(self):
        arrays = []
        for production in self.productions:
            recipe_array = production.get_recipe_array(self.used_items)
            arrays.append(recipe_array)

        master_matrix = np.array([*arrays]).transpose()
        return master_matrix

    @property
    def solution_vector(self):
        solution_array = []
        for item in sorted(self.used_items):
            solution_array.append(self.outputs.get(item, 0))

        solution_vector = np.array(solution_array)
        return solution_vector

    def _find_recipes(self, available_recipes) -> list[Recipe]:
        recipes = []
        for output in self.outputs.keys():
            self._handle_one_output(output, recipes)

        for input_resource in self.inputs:
            recipe = Recipe({}, {input_resource: 1}, 1, None, RecipeName.NO_RECIPE)
            recipes.append(recipe)
        return recipes

    def _handle_one_output(self, output, recipes) -> None:
        for recipe in self.forced_recipes:
            if output in recipe.output_values.keys():
                recipes.append(recipe)
                break
        for recipe in self.available_recipes.values():
            if output in recipe.output_values.keys():
                if recipe in recipes:
                    continue
                recipes.append(recipe)
                break

    def _find_items(self) -> set[Item]:
        items = set()
        for recipe in self.used_recipes:
            for item in recipe.input_values.keys():
                items.add(item)
            for item in recipe.output_values.keys():
                items.add(item)
        return items

    @cached_property
    @auto_format
    def total_power(self):
        power = 0
        for production in self.productions:
            power += production.power_usage
        return power, EnergyUnit.WATT

    @cached_property
    @auto_format
    def power_per_prod(self):
        power = []
        for production in self.productions:
            power.append((production.power_usage, EnergyUnit.WATT))
        return power
