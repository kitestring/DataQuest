# -*- coding: latin -*-

import requests
from bs4 import BeautifulSoup


url = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
response = requests.get(url)

content = response.content

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# The find_all  method will find all occurrences of a tag in the current element, and return a list.
# If we only want the first occurrence of an item, we'll need to index the list to get it.
# Aside from this difference, it behaves the same way as passing in the tag type as an attribute.

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")

# Get the text.
print(p[0].text)