import requests
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=2)

# Latitude & Longitude cooridinates for my address
# (42.091916, -86.479631)
parameters = {'lat': 42.091916, 'lon': -86.479631}

response = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)

# Below is exactly the same request, notice how passing in a dictionary using params makes this much cleaner and easier.
# response = requests.get("http://api.open-notify.org/iss-pass.json?lat=42.091916&lon=-86.479631"  

# pprint is not working right now because the response.contnet is still in json format and needs to be converted to a dictionary.

content = response.content
pp.pprint(content)