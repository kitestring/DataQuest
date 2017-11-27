import requests

headers = {"Authorization": "token 1a69994d902d905d430f995ee92c67b1db24266d"}

response = requests.delete("https://api.github.com/repos/kitestring/learning-about-apis", headers=headers)

status = response.status_code

print(status)