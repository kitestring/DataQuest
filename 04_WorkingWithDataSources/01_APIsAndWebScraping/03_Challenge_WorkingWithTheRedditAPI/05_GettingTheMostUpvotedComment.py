import requests
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

# make get request to get pythons top comments from the reddit API
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

# Convert the json formatted data into a python data structure
python_top = response.json()

# Extract the list containing all of the posts
python_top_articles = python_top['data']['children']

# Put this data into a pandas DataFrame so that it can be more easily worked with
data_lst = []
for post_dict in python_top_articles:
    # this creates a list of dictionaries each with the same keys
    data_lst.append(post_dict['data'])
postdf = pd.DataFrame(data_lst)

# Sort the DataFrame by upvotes
postdf.sort_values(by=['ups'], inplace=True, ascending=False)

# Grab the most upvoted article id
most_upvoted = postdf.iloc[0]['id']

url = "https://oauth.reddit.com/r/python/comments/{}".format(most_upvoted)

response2 = requests.get(url, headers=headers)
comments = response2.json()
# comments is a list
    # the 0th element has the data from the article it self
    # the 1st element contains a dictionary which contains all the comments

comments_list = comments[1]['data']['children']

# Put the call the top level comments into a dataframe
data_lst = []
for comment_dict in comments_list:
    data_lst.append(comment_dict['data'])
commentdf = pd.DataFrame(data_lst)

# Sort the comment data list by upvotes
# The grab the first id which will correspond to the most upvoted comment
commentdf.sort_values(by=['ups'], inplace=True, ascending=False)
most_upvoted_comment = commentdf.iloc[0]['id']