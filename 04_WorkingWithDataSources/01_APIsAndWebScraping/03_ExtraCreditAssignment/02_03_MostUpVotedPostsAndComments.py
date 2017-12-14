# Get the 10 top/new/hot posts in /r/python.
import requests
from oauth2 import authentication
import pprint
import pandas as pd
import time

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)
    
def get_ten_most_upvoted_posts(client_settings, post_type):
    
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
    posts = response.json()
    posts_extracted = posts['data']['children']
    
    posts_lst = []
    for postdict in posts_extracted:
        posts_lst.append(postdict['data'])
    postdf = pd.DataFrame(posts_lst)
    postdf.sort_values(by='ups', ascending= False, inplace=True,)
    return postdf.iloc[0:10]['id']

def get_five_most_upvoted_comments(client_settings, post_id):
    headers = {"Authorization": client_settings['access_token'], "User-Agent": client_settings['user_agent']}
    url = 'https://oauth.reddit.com/r/python/comments/{}'.format(post_id)
    response = requests.get(url, headers=headers)
    all_data = response.json()
    comment_extracted =  all_data[1]['data']['children']
    
    comment_lst = []
    for com in comment_extracted:
        comment_lst.append(com['data'])
    commentdf = pd.DataFrame(comment_lst)
    
    # note if post has no comments this will throw an exception
    # KeyError: 'ups'
    # post id: 7i67m6 had no comments at the time
    commentdf.sort_values(by='ups',ascending=False, inplace=True)
    return commentdf.iloc[0:5]['id']
    
auth = authentication()
if auth.verify_refresh_token() == False:
    print('Authentication Failure')
    exit()


postdict = {}
for i, post_type in enumerate(['new', 'hot', 'top']):
    print('Top 10 most upvoted posts in {}'.format(post_type))
    print('Each with the related top five comments')
    postdict[post_type] = get_ten_most_upvoted_posts(auth.client_settings, post_type)
    for pst in postdict[post_type]:
        print('\npost id:', pst)
        coms = get_five_most_upvoted_comments(auth.client_settings, pst)
        print('\tTop 5 top level comments')
        for com in coms:
            print('\t\tcomment id:', com)
        
    if i < 2:
        # Wait 60 Seconds
        print('\nWaiting 60 Seconds to limit requests per minute\n')
        time.sleep(60)