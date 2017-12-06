import json
import requests
import pprint

# My exercise
print('My exercise\n')
pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

# Latitude & Longitude cooridinates for my address
# (42.091916, -86.479631)
parameters = {'lat': 42.091916, 'lon': -86.479631}

response = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)

json_content = response.content
content = json.loads(json_content)
pp.pprint(content)

# Data Quest exercise
print('\n\n\nData Quest exercise\n')

best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
fast_food_franchise_2 = json.loads(fast_food_franchise_string)
