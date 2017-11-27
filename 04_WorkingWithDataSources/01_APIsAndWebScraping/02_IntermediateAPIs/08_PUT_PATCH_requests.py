import requests

payload = {'name': 'learning-about-apis', 'description': 'My First repo made using a POST request. Now I will edit this repo using a PATCH request'}
headers = {"Authorization": "token 1a69994d902d905d430f995ee92c67b1db24266d"}

response = requests.patch("https://api.github.com/repos/kitestring/learning-about-apis", json=payload, headers=headers)
status = response.status_code
print(status)