# -*- coding: latin -*-

import requests
from bs4 import BeautifulSoup


url = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
response = requests.get(url)

content = response.content

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
p_text = p.text
print('This is the text inside the p tag:', p_text)


# This is the text inside the title tag
title_text = parser.head.title.text
print('This is the text inside the title tag:', title_text)


# This method will find all occurrences of a tag in the current element, and return a list.

If we only want the first occurrence of an item, we'll need to index the list to get it. Aside from this difference, it behaves the same way as passing in the tag type as an attribute.
