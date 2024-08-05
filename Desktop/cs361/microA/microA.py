import json
import time
import os

def file_change(file):
    oldt = os.path.getmtime(file)
    while True:
        nt = os.path.getmtime(file)
        if nt != oldt:
            return 1


while True:
    if file_change('ingredientCompare.json') == 1:
        ingredients = set()
        needs = set()
        with open('ingredientCompare.json', 'r') as inputfile:
            file_objs = json.load(inputfile)

        for i in file_objs['ingredients']:
            ingredients.add(i['name'])

        for r in file_objs['recipe']:
            for ingredient in r['ingredients']:
                if ingredient not in ingredients:
                    needs.add(ingredient)
                
        needs = list(needs)
        ingredients = list(ingredients)
        
        data = {
            "Don't Have": needs,
            "Have": ingredients
        }

        json_data = json.dumps(data, indent = 4)

        with open("ingredient.json", 'w') as outfile:
            outfile.write(json_data)

        print("Updated")
    

