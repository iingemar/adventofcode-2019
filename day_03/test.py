import unittest
from main import FuelManagementSystem


class TestFuelManagementSystem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(FuelManagementSystem('R8,U5,L5,D3\nU7,R6,D4,L4'), 6)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFuelManagementSystem)
    unittest.TextTestRunner(verbosity=2).run(suite)
