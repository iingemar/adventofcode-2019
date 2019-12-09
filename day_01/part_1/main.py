from __future__ import division
import math


class SpacecraftModule:
    def __init__(self, mass):
        self.mass = mass
        self.fuel = self.calculate_fuel()

    def calculate_fuel(self):
        return math.floor(self.mass / 3) - 2


def get_modules():
    with open('input.txt') as f:
        content = f.readlines()
    return [SpacecraftModule(int(x.strip())) for x in content]


if __name__ == '__main__':
    modules = get_modules()
    fuel_requirements = sum(m.fuel for m in modules)
    print(fuel_requirements)

