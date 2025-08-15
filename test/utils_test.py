import unittest
from utils import add_numbers, greet, calculate_mean

class UtilsTest(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_calculate_mean(self):
        self.assertAlmostEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(calculate_mean([10, 20, 30]), 20.0)
        self.assertAlmostEqual(calculate_mean([0, 0, 0]), 0.0)

if __name__ == "__main__":
    unittest.main()
