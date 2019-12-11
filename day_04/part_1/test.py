import unittest
from main import PasswordChecker


class TestPasswordChecker(unittest.TestCase):
    def test_1(self):
        self.assertEqual(PasswordChecker(111111).is_ok(), True)
        self.assertEqual(PasswordChecker(223450).is_ok(), False)
        self.assertEqual(PasswordChecker(123789).is_ok(), False)
        self.assertEqual(PasswordChecker(122345).is_ok(), True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPasswordChecker)
    unittest.TextTestRunner(verbosity=2).run(suite)
