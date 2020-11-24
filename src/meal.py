import requests


class Meal:
    def search_meal_by_name(self, name):
        name_input = name.replace(' ', '_')
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name_input}").json()
        return meal['meals'][0]

    def search_meal_by_id(self, id):
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}").json()
        return meal['meals'][0]

    def get_random_meal(self):
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/random.php").json()
        return meal['meals'][0]

    def get_meal_categories(self):
        categories = requests.get(f"https://www.themealdb.com/api/json/v1/1/categories.php").json()
        return categories['categories']

    def get_ingredients(self):
        ingredients = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?i=list").json()
        return ingredients['meals']

    def get_categories(self):
        categories = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?c=list").json()
        return categories['meals']

    def get_area(self):
        area = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?a=list").json()
        return area['meals']

    def filter_by_main_ingredient(self, ingredient):
        ingredient_input = ingredient.replace(' ', '_')
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient_input}").json()
        return meal['meals']

    def filter_by_category(self, category):
        category_input = category.replace(' ', '_')
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category_input}").json()
        return meal['meals']

    def filter_by_area(self, area):
        area_input = area.replace(' ', '_')
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area_input}").json()
        return meal['meals']


meal = Meal()

print(len(meal.get_area()))