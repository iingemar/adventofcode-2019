import unittest
from main import SpacecraftModule


class TestFuelCalculations(unittest.TestCase):
    def test_mass_12(self):
        self.assertEqual(SpacecraftModule(12).fuel, 2)

    def test_mass_14(self):
        self.assertEqual(SpacecraftModule(14).fuel, 2)

    def test_mass_1969(self):
        self.assertEqual(SpacecraftModule(1969).fuel, 654)

    def test_mass_100756(self):
        self.assertEqual(SpacecraftModule(100756).fuel, 33583)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFuelCalculations)
    unittest.TextTestRunner(verbosity=2).run(suite)
