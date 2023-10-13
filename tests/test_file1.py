import unittest
from module1 import add_numbers  # Import the function you want to test

class TestModule1Functions(unittest.TestCase):

    def test_add_numbers_positive(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5, "Adding 2 and 3 should equal 5")

    def test_add_numbers_negative(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5, "Adding -2 and -3 should equal -5")

    def test_add_numbers_mixed(self):
        result = add_numbers(5, -3)
        self.assertEqual(result, 2, "Adding 5 and -3 should equal 2")

    def test_add_numbers_zero(self):
        result = add_numbers(0, 7)
        self.assertEqual(result, 7, "Adding 0 and 7 should equal 7")

if __name__ == '__main__':
    unittest.main()
