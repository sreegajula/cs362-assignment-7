import unittest
from leapyear import check_leap

class TestLeap(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(check_leap(2020), 1)
        self.assertEqual(check_leap(2032), 1)
        self.assertEqual(check_leap(2012), 1)

class TestNotLeap(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(check_leap(2019), 0)
        self.assertEqual(check_leap(2031), 0)
        self.assertEqual(check_leap(2011), 0)
