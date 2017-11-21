import requests


response = requests.get("http://api.open-notify.org/iss-pass")
status_code = response.status_code
print(status_code)