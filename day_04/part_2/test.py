import unittest
from main import PasswordChecker


class TestPasswordChecker(unittest.TestCase):
    def test_1(self):
        self.assertEqual(PasswordChecker(112233).is_ok(), True)
        self.assertEqual(PasswordChecker(123444).is_ok(), False)
        self.assertEqual(PasswordChecker(111122).is_ok(), True)
        self.assertEqual(PasswordChecker(112223).is_ok(), False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPasswordChecker)
    unittest.TextTestRunner(verbosity=2).run(suite)
