import requests
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

# Latitude & Longitude cooridinates for my address
# (42.091916, -86.479631)
parameters = {'lat': 42.091916, 'lon': -86.479631}

response = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)

json_data = response.json()
first_pass_duration = json_data['response'][0]['duration']
print('All Data Recieved')
pp.pprint(json_data)

print('\nFirst Pass Duration')
print(first_pass_duration)