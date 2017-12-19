import requests
import pprint

# Note, it seems that this will work for basically any website

url = "https://en.wikipedia.org/wiki/List_of_Chicago_Bears_seasons"
# url = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
response = requests.get(url)

content = response.content

pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)

pp.pprint(content)