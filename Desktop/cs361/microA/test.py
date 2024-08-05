import json
import time

data = {
"ingredients": [
    {
    "id": "a7461489-5190-4c13-b520-0ef6b01ef604",
    "name": "apples",
    "quantity": "2 small",
    "expirationDate": "2024-08-08"
    },
    {
    "id": "5eb281ea-8baa-4582-bae2-1677efc55af3",
    "name": "salmon",
    "quantity": "1",
    "expirationDate": "2024-08-07"
    },
    {
    "id": "5e3281ea-8baa-4582-bae2-1677efc55af3",
    "name": "miso",
    "quantity": "1",
    "expirationDate": "2024-08-07"
    }
],
"recipe": [
    {
        "id": "2919c07c-c16c-422b-85fb-ada4b029f7e1",
        "name": "miso salmon",
        "ingredients": [ "miso", "salmon", "soy sauce", "mirin", "sesame oil" ],
        "instructions": "1. combine all ingredients to make marinade 2. marinade salmon overnight 3. bake at 350F for 30 minutes"
        }
]
}

json_data = json.dumps(data, indent = 4)

with open('ingredientCompare.json', 'w') as outfile:
    outfile.write(json_data)

time.sleep(3)

data = {
"ingredients": [
    {
    "id": "a7461489-5190-4c13-b520-0ef6b01ef604",
    "name": "apples",
    "quantity": "2 small",
    "expirationDate": "2024-08-08"
    },
    {
    "id": "5eb281ea-8baa-4582-bae2-1677efc55af3",
    "name": "salmon",
    "quantity": "1",
    "expirationDate": "2024-08-07"
    },
    {
    "id": "5e3281ea-8baa-4582-bae2-1677efc55af3",
    "name": "miso",
    "quantity": "1",
    "expirationDate": "2024-08-07"
    },
    {
    "id": "5e3281fa-8baa-4582-bae2-1677efc55af3",
    "name": "soy sauce",
    "quantity": "1",
    "expirationDate": "2024-08-07"
    }
],
"recipe": [
    {
        "id": "2919c07c-c16c-422b-85fb-ada4b029f7e1",
        "name": "miso salmon",
        "ingredients": [ "miso", "salmon", "soy sauce", "mirin", "sesame oil" ],
        "instructions": "1. combine all ingredients to make marinade 2. marinade salmon overnight 3. bake at 350F for 30 minutes"
        }
]
}

json_data = json.dumps(data, indent = 4)

with open('ingredientCompare.json', 'w') as outfile:
    outfile.write(json_data)
time.sleep(1)
with open('ingredient.json', 'r') as infile:
    datan = json.load(infile)

haves = datan['Have']

print(haves)
