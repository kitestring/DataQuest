import requests
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

headers = {"Authorization": "token 1a69994d902d905d430f995ee92c67b1db24266d"}

response = requests.get("https://api.github.com/repos/octocat/Hello-World", headers=headers)
hello_world = response.json()
pp.pprint(hello_world)