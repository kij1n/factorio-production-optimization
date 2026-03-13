import json


def load_const():
    constants = {}
    with open("constants.json") as f:
        constants = json.load(f)
    return constants
