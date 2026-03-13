from oil_processing import oil_processing

target_values = [326.25, 1603.66, 30260.24]
heavy_oil, light_oil, aop = oil_processing(*target_values)
print(f"Heavy oil cracking: {heavy_oil} machines")
print(f"Light oil cracking: {light_oil} machines")
print(f"Advanced oil processing: {aop} machines")

# setup a factory, disc where how many radios does each have, with what modules
# speed of machines, their quality, quality of radios and modules
