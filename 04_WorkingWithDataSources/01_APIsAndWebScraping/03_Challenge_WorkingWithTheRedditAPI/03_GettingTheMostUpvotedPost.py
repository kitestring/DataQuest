import requests
import pandas as pd

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
    data_lst.append(post_dict['data'])
postdf = pd.DataFrame(data_lst)
print(postdf.columns)

# Sort the DataFrame by upvotes
postdf.sort_values(by=['ups'], inplace=True, ascending=False)

# Grab the most upvoted article id
most_upvoted = postdf.iloc[0]['id']

