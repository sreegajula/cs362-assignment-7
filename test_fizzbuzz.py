import unittest
from fizzbuzz import test_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(test_buzz(3), "Fizz")
        self.assertEqual(test_buzz(9), "Fizz")
        self.assertEqual(test_buzz(12), "Fizz")

if __name__ == '__main__':
    unittest.main()