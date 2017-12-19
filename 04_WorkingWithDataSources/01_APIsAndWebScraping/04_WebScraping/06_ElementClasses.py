from bs4 import BeautifulSoup
import requests


# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
first_inner_paragraph_text = first_inner_paragraph.text
second_inner_paragraph = parser.find_all("p", class_="inner-text")[1]
second_inner_paragraph_text = second_inner_paragraph.text
print('first_inner_paragraph_text:', first_inner_paragraph_text)
print('second_inner_paragraph_text:', second_inner_paragraph_text)

first_outer_paragraph = parser.find_all("p", class_="outer-text")[0]
first_outer_paragraph_text = first_outer_paragraph.text
print('first_outer_paragraph_text:', first_outer_paragraph_text)