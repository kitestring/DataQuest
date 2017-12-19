import requests
from bs4 import BeautifulSoup

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

second_paragraph = parser.find_all('p', id="second")[0]
second_paragraph_text = second_paragraph.text
print(second_paragraph_text)

paragraphs = parser.find_all("p",)

# You can also iterate over the tabs to get the id
for paragraph in paragraphs:
    print(paragraph['id'])
    
