import requests

# until I learn more about oauth and can get my own authentication token I'll not be able to do do this for real
# :( that sucks... for now.

# Instructions...
    # Retrieve the /r/python subreddit's top posts for the past day.
        # Make a GET request to https://oauth.reddit.com/r/python/top using the get method of the requests library. See the documentation for the /r/python/top endpoint if you need help.
        # Pass in the header information we showed you earlier in this section.
        # To retrieve only the top posts for the past day, pass in a query parameter t (for "time") and set its value to the string day.
    # Use the json method on the response to get the JSON response data.
    # Assign the JSON response data to the variable python_top.

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}

response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)


python_top = response.json()
 
print(python_top)