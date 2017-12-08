import requests
from oauth2 import authentication

auth = authentication()
auth.get_new_token()

headers = {"Authorization": auth.client_settings['access_token'], "User-Agent": auth.client_settings['user_agent']}
response = requests.get("https://oauth.reddit.com", headers=headers)

status = response.status_code
print(status)
# This returned a status code of 200 which means everything went okay, and the server returned a result of ok