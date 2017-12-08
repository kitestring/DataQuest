# Get the 10 top/best/new/hot posts in /r/python.
import requests
from oauth2 import authentication

auth = authentication()
auth.get_new_token()

