with open('recipes.txt', encoding='UTF-8') as f:
    data = f.read()

recipes = data.strip().split('\n\n')
cook_book = {}

for recipe in recipes:
    recipe = recipe.split('\n')
    cook_book[recipe[0]] = []
    for ingredients in recipe[2:]:
        ingredients = ingredients.split('|')
        one_ingredient = {
            'ingredient_name': ingredients[0],
            'quantity': ingredients[1],
            'measure': ingredients[2]
        }
        cook_book[recipe[0]].append(one_ingredient)


def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    for dish in dishes:
        list_ingredients = cook_book.get(dish)
        for ingredient in list_ingredients:
            if dict_ingredients.get(ingredient['ingredient_name']) is None:
                dict_ingredients[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': (int(ingredient['quantity']) * person_count)}
            else:
                dict_ingredients[ingredient['ingredient_name']]['quantity'] = (
                        dict_ingredients[ingredient['ingredient_name']]['quantity']
                        + (int(ingredient['quantity']) * person_count))

    print(dict_ingredients)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
