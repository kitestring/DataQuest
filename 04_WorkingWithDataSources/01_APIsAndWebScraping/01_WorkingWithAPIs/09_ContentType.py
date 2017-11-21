import requests
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

# Latitude & Longitude cooridinates for my address
# (42.091916, -86.479631)
parameters = {'lat': 42.091916, 'lon': -86.479631}

response = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)

headers = response.headers
pp.pprint(headers['Content-Type'])
