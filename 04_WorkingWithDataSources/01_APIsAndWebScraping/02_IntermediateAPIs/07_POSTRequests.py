import requests

payload = {'name': 'learning-about-apis', 'description': 'My First repo made using a POST request'}
headers = {"Authorization": "token 1a69994d902d905d430f995ee92c67b1db24266d"}

response = requests.post("https://api.github.com/user/repos/", json=payload, headers=headers)
status = response.status_code
print(status)