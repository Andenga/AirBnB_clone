import unittest
from module2 import calculate_average  # Import the function you want to test

class TestModule2Functions(unittest.TestCase):

    def test_calculate_average_empty_list(self):
        numbers = []
        result = calculate_average(numbers)
        self.assertEqual(result, 0, "Calculating the average of an empty list should be 0")

    def test_calculate_average_single_value(self):
        numbers = [5]
        result = calculate_average(numbers)
        self.assertEqual(result, 5, "Calculating the average of a single value list should be the value itself")

    def test_calculate_average_positive_values(self):
        numbers = [3, 6, 9, 12, 15]
        result = calculate_average(numbers)
        self.assertEqual(result, 9, "Calculating the average of positive values should be 9")

    def test_calculate_average_mixed_values(self):
        numbers = [-2, 4, 0, 7, -5]
        result = calculate_average(numbers)
        self.assertEqual(result, 0.8, "Calculating the average of mixed values should be 0.8")

if __name__ == '__main__':
    unittest.main()
