from bs4 import BeautifulSoup
import pandas as pd
import requests


# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the Total Plays for the New England Patriots, and assign the result to patriots_total_plays_count.
# Find the Total Yards for the Seahawks, and assign the result to seahawks_total_yards_count.

# First get all the id's in the tr (table row) tag
tr = parser.find_all('tr')
id_lst = ['#' + item['id'] for item in tr]

table_data = []

# Iterate through each tr id
# further parse data either by th or td (table header or table data)
for column_index, column_id in enumerate(id_lst):
    column = parser.select(column_id)[0]
    if column_id == '#teams':
        values = column.select('th')
    else:
        values = column.select('td')
    
    # For each parsed table row id assign each value to a list of dictionaries 
    # that easily lends it self to DataFrame creation
    # Note, values is a list of each id value.
    # The 0th item is excluded because it is the header.
    for value_index, value in enumerate(values[1:]):
        if column_index == 0:
            table_data.append({})
        table_data[value_index][column_id[1:]] = value.text

superbowl_twentyfourteen = pd.DataFrame(table_data)
superbowl_twentyfourteen.set_index('teams', inplace=True)

patriots_total_plays_count = superbowl_twentyfourteen.loc['NWE']['total-plays']
seahawks_total_yards_count = superbowl_twentyfourteen.loc['SEA']['total-yards']

print('patriots_total_plays_count:', patriots_total_plays_count)
print('seahawks_total_yards_count:', seahawks_total_yards_count)
