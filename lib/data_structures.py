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
    names = [items["name"] for items in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spice = [food for food in spicy_foods if food["heat_level"] > 5 ]
    return spice

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = food["heat_level"]
        emoji = "🌶" * heat

        print(f"{name} ({cuisine}) | Heat Level: {emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5 :
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    heat = [levels["heat_level"] for levels in spicy_foods]
    average = sum(heat) / len(spicy_foods)
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    new_list = [food for food in spicy_foods]
    new_list.append(spicy_food)
    return new_list
