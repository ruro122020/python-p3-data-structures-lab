spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food_obj["name"] for food_obj in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food_obj for food_obj in spicy_foods if food_obj["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
  for food_obj in spicy_foods:
      print(f"{food_obj['name']} ({food_obj['cuisine']}) | Heat Level: {'🌶' * food_obj['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_obj in spicy_foods:
        if food_obj["cuisine"] == cuisine:
            return food_obj
    pass

print(get_spicy_food_by_cuisine(spicy_foods, 'American'))

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
