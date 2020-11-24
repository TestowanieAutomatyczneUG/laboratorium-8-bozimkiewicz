import unittest
from src.meal import Meal


class TestMeal(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def test_search_meal_by_name(self):
        self.assertEqual(self.temp.search_meal_by_name('arrabiata')['idMeal'], '52771')

    def test_search_meal_by_id(self):
        self.assertEqual(self.temp.search_meal_by_id('52771')['strMeal'], 'Spicy Arrabiata Penne')

    def test_get_meal_categories(self):
        self.assertEqual(len(self.temp.get_meal_categories()), 14)

    def test_get_ingredients(self):
        self.assertEqual(len(self.temp.get_ingredients()), 571)

    def test_get_categories(self):
        self.assertEqual(len(self.temp.get_categories()), 14)

    def test_get_area(self):
        self.assertEqual(len(self.temp.get_area()), 25)

    def test_filter_by_main_ingredient(self):
        self.assertEqual(self.temp.filter_by_main_ingredient('chicken breast')[0]['strMeal'], 'Chick-Fil-A Sandwich')

    def test_filter_by_category(self):
        self.assertEqual(self.temp.filter_by_category('seafood')[0]['strMeal'], 'Baked salmon with fennel & tomatoes')

    def test_filter_by_area(self):
        self.assertEqual(self.temp.filter_by_area('canadian')[0]['strMeal'], 'BeaverTails')

    def tearDown(self):
        self.temp = None
