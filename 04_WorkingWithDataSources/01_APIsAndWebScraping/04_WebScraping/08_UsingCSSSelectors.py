from bs4 import BeautifulSoup
import requests


# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the outer-text class.
outer_text = parser.select(".outer-text")
first_outer_text = outer_text[0].text

# Print the text of the first paragraph (the first element with the outer-text class).
print(first_outer_text)

second = parser.select('#second')
second_text = second[0].text
print(second_text)