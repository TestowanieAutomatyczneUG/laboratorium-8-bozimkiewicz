import unittest
from src.meal import Meal


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def tearDown(self):
        self.temp = None
