import unittest
from leapyear import check_leap

class TestFizz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(check_leap(2020), 1)
        self.assertEqual(check_leap(2030), 0)
        self.assertEqual(check_leap(2012), 1)
