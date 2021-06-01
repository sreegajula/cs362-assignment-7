import unittest
from fizzbuzz import test_buzz


class TestFizz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(test_buzz(3), "Fizz")
        self.assertEqual(test_buzz(9), "Fizz")
        self.assertEqual(test_buzz(12), "Fizz")

class TestBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(test_buzz(5), "Buzz")
        self.assertEqual(test_buzz(10), "Buzz")
        self.assertEqual(test_buzz(20), "Buzz")


if __name__ == '__main__':
    unittest.main()

