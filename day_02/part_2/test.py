import unittest
from main import Intcode


class TestIntcode(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Intcode('1,0,0,0,99').get_result(), '2,0,0,0,99')

    def test_2(self):
        self.assertEqual(Intcode('2,3,0,3,99').get_result(), '2,3,0,6,99')

    def test_3(self):
        self.assertEqual(Intcode('2,4,4,5,99,0').get_result(), '2,4,4,5,99,9801')

    def test_4(self):
        self.assertEqual(Intcode('1,1,1,4,99,5,6,0,99').get_result(), '30,1,1,4,2,5,6,0,99')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIntcode)
    unittest.TextTestRunner(verbosity=2).run(suite)