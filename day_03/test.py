import unittest
from main import FuelManagementSystem


class TestFuelManagementSystem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(FuelManagementSystem('R8,U5,L5,D3\nU7,R6,D4,L4').closest_intersection, 6)

    def test_2(self):
        path = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
        self.assertEqual(FuelManagementSystem(path).closest_intersection, 159)

    def test_3(self):
        path = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
        """
        self.assertEqual(FuelManagementSystem(path).closest_intersection, 135)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFuelManagementSystem)
    unittest.TextTestRunner(verbosity=2).run(suite)
