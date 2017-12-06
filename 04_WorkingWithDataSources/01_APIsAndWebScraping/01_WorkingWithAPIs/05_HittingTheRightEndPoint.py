import requests

response = requests.get("http://api.open-notify.org/iss-pass.json")
status_code = response.status_code
print(status_code)