# Get the 10 top/new/hot posts in /r/python.
import requests
from oauth2 import authentication
import pprint
import pandas as pd
import time

# pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)
    
def get_10_most_upvoted_posts(client_settings, post_type):
    
    params = {'top': {"t": "year", 'limit': 100},
             'hot': {'g': 'US', 'limit': 100},
             'new': {'limit': 100}}
    
    endpoint_url = {'top': 'https://oauth.reddit.com/r/python/top',
                     'hot': 'https://oauth.reddit.com/r/python/hot',
                     'new': 'https://oauth.reddit.com/r/python/new'}
    
    if not post_type in params:
        return "Invalid Post Type"
    
    headers = {"Authorization": client_settings['access_token'], "User-Agent": client_settings['user_agent']}
    
    response = requests.get(endpoint_url[post_type], headers=headers, params=params[post_type])
    print('Response Status Code:', response.status_code)
    posts = response.json()
    posts_extracted = posts['data']['children']
    
    posts_lst = []
    for postdict in posts_extracted:
        posts_lst.append(postdict['data'])
    postdf = pd.DataFrame(posts_lst)
    postdf.sort_values(by='ups', ascending= False, inplace=True,)
    return postdf.iloc[0:10]['id']

def get_comment_tree(client_settings, post_id='63dkmq'):
    headers = {"Authorization": client_settings['access_token'], "User-Agent": client_settings['user_agent']}
    url = 'https://oauth.reddit.com/r/python/comments/{}'.format(post_id)
    response = requests.get(url, headers=headers)
    print('Response Status Code:', response.status_code)
    return response.json()
    
auth = authentication()
if auth.verify_refresh_token() == False:
    print('Authentication Failure')
    exit()


# postdict = {}
# for i, post_type in enumerate(['new', 'hot', 'top']):
#     print(post_type)
#     postdict[post_type] = get_10_most_upvoted_posts(auth.client_settings, post_type)
#     print(postdict[post_type])
#     
#     if i < 2:
#         # Wait 5 Seconds
#         print('\nWaiting 5 Seconds to limit requests per unit time\n')
#         time.sleep(5)
        
#t est = get_comment_tree(auth.client_settings)
# print(test[1]['data'])