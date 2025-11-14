import unittest
from age import categorize_by_age

class TestAgeCategorization(unittest.TestCase):
    def test_child_category(self):
        self.assertEqual(categorize_by_age(5), "Child")
        self.assertEqual(categorize_by_age(9), "Child")
    def test_teenager_category(self):
        self.assertEqual(categorize_by_age(13), "Teenager")
        self.assertEqual(categorize_by_age(18), "Teenager")
    def test_adult_category(self):
        self.assertEqual(categorize_by_age(24), "Adult")
        self.assertEqual(categorize_by_age(64), "Adult")
    def test_goldenage_category(self):
        self.assertEqual(categorize_by_age(65), "Golden Age")
        self.assertEqual(categorize_by_age(120), "Golden Age")
    def test_error(self):
        self.assertEqual(categorize_by_age(-1), f"Invalid Age: -1")
        self.assertEqual(categorize_by_age(-121), f"Invalid Age: -121")
        self.assertEqual(categorize_by_age(121), f"Invalid Age: 121")