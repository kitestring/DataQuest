import requests
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

response = requests.get("http://api.open-notify.org/astros.json")

json_data = response.json()
print('Received Data')
pp.pprint(json_data)
in_space_count = json_data['number']
print('\nThere are currently {} people in space right now'.format(in_space_count))
print('str%sing number: %d' % ('moresuff', 55))