from __future__ import division
import math


class SpacecraftModule:
    def __init__(self, mass):
        self.mass = mass
        self.fuel = 0
        self.calculate_fuel(mass)

    def calculate_fuel(self, input_mass):
        fuel = math.floor(input_mass / 3) - 2
        if fuel > 0:
            print(fuel)
            self.fuel = self.fuel + fuel
            self.calculate_fuel(fuel)


def get_modules():
    with open('input.txt') as f:
        content = f.readlines()
    return [SpacecraftModule(int(x.strip())) for x in content]


if __name__ == '__main__':
    modules = get_modules()
    fuel_requirements = sum(m.fuel for m in modules)
    print(fuel_requirements)

