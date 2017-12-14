# -*- coding: latin -*-

# The goal is to mine the win loss records for every time and for every season 
# for the entire history of the NFL.
# data will be scraped from https://en.wikipedia.org/wiki/{Team_Name_City}_seasons

from pandas import DataFrame
from bs4 import BeautifulSoup
import requests

def determineheaderstyle(lsts):
    second_row_headers = lsts[1]
    len_second_row_headers = len(second_row_headers)
    # The difference is that some data sets have a Win% column that is 
    # inserted at index = 9. This only affects the Post Season Result
    # index, it will shift from index = 9 to index = 10. 
    
    if len_second_row_headers == 4:
        # When len_second_row_headers == 4 Win% column is not present
        return {'Year': 0, 'Wins': 6, 'Losses': 7, 'Ties': 8, 'Finish': 5, 'Post_Season_Results':9}
    elif len_second_row_headers == 5:
        # When len_second_row_headers == 5 Win% is not present
        return {'Year': 0, 'Wins': 6, 'Losses': 7, 'Ties': 8, 'Finish': 5, 'Post_Season_Results':10}
    
    # Just found a problem with the 'Post_Season_Results' columns as each individual game 
    # is separated by a '\n' as such each game will have a seperate element
    # I'm not fixing this now it's not that important
    # Right now the post season will just verify if the team went or not, not the exact results

def remove_leading_empties(lst):
    while lst[0] == '' and len(lst) > 1:
        lst.remove('')
    return lst

def verifyrowdata(lst):
    # All rows whose 0th & 1st elements are not the same 4 digit integer return False
    try:
        season_int =  int(lst[0][0:4])
        team_int = int(lst[1][0:4])
        if season_int == team_int:
            return True
        else:
            return False
    except ValueError:
        return False
    
def cleanlsts(lsts):
    # I.) returns a list of list with the following formating:
        # 1.) Each list represents a row
        # 2.) Element in a sublist represents a value witihn a row
        # 3.) The Headers are 1 of 2 possibilities as follows: (Ignoring the elements prior to 'Season')
            # ['Season', 'Team', 'League', 'Conference', 'Division', 'Finish', 'Wins', 'Losses', 'Ties'', 'Postseason results', ect...]
            # ['Season', 'Team', 'League', 'Conference', 'Division', 'Finish', 'Wins', 'Losses', 'Ties'', 'Win%', 'Postseason results', ect...]
    # II.) All rows that fail on the basis of verifyrowdata() are excluded
    # III.) Data prior to 1933 is formatted differently, 
        # these rows wrap to the following row
        # All rows that are from prior to 1933, the following
        # row will be extended on to the current
    
    # Retain the headers            
    new_lsts = lsts[0:2]
    attch_next_row = False
       
    for lst in lsts[2:]:
        if attch_next_row == True:
            # The preceding row is verified to be prior to 1933
            # and there for will be extended to the previous row
            attch_next_row = False
            new_lsts[-1].extend(['',''])
            new_lsts[-1].extend(lst)
        elif verifyrowdata(lst) == True:
            # This row has been verified to have real data
            if int(lst[0][0:4]) < 1933:
                # This row has been verified to be prior to 1933
                attch_next_row = True
            new_lsts.append(lst)
        else:
            # This row contains no useful data
            attch_next_row = False
    return new_lsts

def buildlistofdicts(lsts, key_dict, starting_list_index=2):
    # Assumes the first two lists contain poorly formatted headers
    # lsts = contains the list of lists that will be converted to a list of dictionarires
    # keys_dict = keys: strings that will be used to create the keys in the resulting dictist
        # values: the index numbers to access the elements in the sublist that will be the values in the dictlst
    dictlst = []
    for lst in lsts[starting_list_index:]:
        temp_dict = {}
        for key, index in key_dict.items():
            
            # If the index is out of range then None will be assigned to the corresponding key
            try: 
                temp_dict[key] = lst[index]
            except IndexError:
                temp_dict[key] = None
                
        dictlst.append(temp_dict)
        
    return dictlst

                        
# url = 'https://en.wikipedia.org/wiki/List_of_Miami_Dolphins_seasons'
url = "https://en.wikipedia.org/wiki/List_of_Chicago_Bears_seasons"
# url = 'https://en.wikipedia.org/wiki/List_of_Green_Bay_Packers_seasons'
# url = 'https://en.wikipedia.org/wiki/List_of_Baltimore_Ravens_seasons'
# url = 'https://en.wikipedia.org/wiki/List_of_Pittsburgh_Steelers_seasons'
response = requests.get(url)

content = response.content

# Initialize the parser, and pass in the content we grabbed earlier.
# I'm guessing that the parser is deterimnie from the DOCTYPE
parser = BeautifulSoup(content, 'html.parser')

# It looks like this has gotten me what I need.
# I'll just have to write some logic so the I can 
# structure it.
tabs = parser.find_all('table')
season_record_row_strings = None

for tab in tabs:
    # Iterates through each table looking for the "season-by-season" win loss data table
    # The table with "Season", "Team", "League", & "Conference" in the 1st 10 elements is the "season-by-season" win loss data table
    temp = tab.text.split('\n')

    if 'Season' in temp[0:10] and 'Team' in temp[0:10] and 'League' in temp[0:10] and 'Conference' in temp[0:10]:
        # each table row is delimited by 3 new line characters
        season_record_row_strings = tab.text.split('\n\n\n')

# If the season is not found or formatted differently then raise an exception        
if season_record_row_strings == None:
    raise Exception('Unexpected Data Formatting: The string = "Season" was not found in the home value.')
        
# Structre data: list if libraries that can be converted into a pd DataFrame
    # 1) Each row terminates with '\n\n\n' (with few exceptions)
    # 2) Within each row each value is separated by a '\n'

# Splits the primary string into a list of strings each list item are the values for a given row
# Iterate through each row string and split into individual values
season_record_lsts = [row_str.split('\n') for row_str in season_record_row_strings]

# Clean up the data set
# Removing leading '' elements
season_record_lsts[:] = [remove_leading_empties(sublist) for sublist in season_record_lsts]
# All rows of a single element contain no win loss data and are thus removed
season_record_lsts[:] = [sublist for sublist in season_record_lsts if len(sublist) > 1] 
# All rows whose 0th & 1st elements are not the same 4 digit integer are culled
cleaned_season_record_lsts = cleanlsts(season_record_lsts)

# Restructure data into list of dictionaries
# each dictionary is a row of data where the key = header and value = value
key_dict = determineheaderstyle(cleaned_season_record_lsts)
seasons_lst_of_dicts = buildlistofdicts(cleaned_season_record_lsts, key_dict)

# Create DataFrame for easy data manuplation
season_df = DataFrame(seasons_lst_of_dicts)
print(season_df)

