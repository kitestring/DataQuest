import requests
from oauth2 import authentication

auth = authentication()
if auth.verify_refresh_token() == False:
    print('Authentication Failure')
    exit()

payload = {'thing_id': 't3_shttps://www.reddit.com/r/CHIBears/comments/7iwd11/holy_shit_we_actually_look_like_a_football_team/tuff', 
            'text': "Its always good to get a win, especially of that magnitude. However its hard to get excited or feel optomistic about this team"}   
 
headers = {"Authorization": auth.client_settings['access_token'], "User-Agent": auth.client_settings['user_agent']}
url = 'https://oauth.reddit.com/api/comment'

response = requests.post(url, headers=headers, json=payload)
print('Response Status Code:', response.status_code)
print('I got a 403 which means that I do not have access to do this.')
print('I think I will move on to web scraping')

# https://www.reddit.com/r/CHIBears/comments/7iwd11/holy_shit_we_actually_look_like_a_football_team/

# payload = {'dir': 1, 'id': most_upvoted_comment}
# 
# response3 = requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=headers)