import requests

# The first endpoint we'll look at on OpenNotify is the iss-now.json endpoint. 
# This endpoint gets the current latitude and longitude position of the ISS. A data 
# set wouldn't be a great fit for this task because the information changes often, 
# and involves some calculation on the server.


# Make a get request to get the latest position of the ISS from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
print(status_code)

