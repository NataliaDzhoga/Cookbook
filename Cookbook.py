with open ('recipes.txt', encoding='UTF-8') as f:
    data = f.read()

recipes = data.strip().split('\n\n')
cook_book = {}

for recipe in recipes:
    recipe = recipe.split('\n')
    cook_book[recipe[0]] = []
    for ingredients in recipe[2:]:
        ingredient = ingredients.split('|')
        d = {}
        d['ingredient_name'] = ingredient[0]
        d['quantity'] = ingredient[1]
        d['measure'] = ingredient[2]
        cook_book[recipe[0]].append(d)

print(cook_book)
