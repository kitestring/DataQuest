# -*- coding: latin -*-

# The goal is to mine the win loss records for every time and for every season 
# for the entire history of the NFL.
# data will be scraped from https://en.wikipedia.org/wiki/{Team_Name_City}_seasons

import os
import pprint
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

def determineheaderstyle(lsts, team_name):
    second_row_headers = lsts[1]
    len_second_row_headers = len(second_row_headers)
    # The difference is that some data sets have a Win% column that is 
    # inserted at index = 9. This only affects the Post Season Result
    # index, it will shift from index = 9 to index = 10. 
        # Furthermore, the Post_Season_Results index is just the starting
        # index number and not necessarily the whole portion of  the data
        # this will be handled in a later method
    
    if len_second_row_headers == 4 or team_name == 'New_York_Giants' or team_name == 'San_Francisco_49ers':
        # When len_second_row_headers == 4 Win% column is not present
        return {'Year': 0, 'Wins_RS': 6, 'Losses_RS': 7, 'Ties_RS': 8, 'Finish': 5, 'Post_Season_Results':9}
    elif len_second_row_headers == 5:
        # When len_second_row_headers == 5 Win% is not present
        return {'Year': 0, 'Wins_RS': 6, 'Losses_RS': 7, 'Ties_RS': 8, 'Finish': 5, 'Post_Season_Results':10}
    
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
    
def cleanlsts(lsts, team = None):
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
    
    # define logic exceptions
    logic_exception_year = {'Cleveland_Browns': 1949,
                        'Los_Angeles_Rams': 1936,
                        'San_Francisco_49ers': 1949}
    
    logic_exception = team in logic_exception_year
    
    # Retain the headers            
    new_lsts = lsts[0:2]
    attch_next_row = False
       
    for lst in lsts[2:]:
#         if team == 'Los_Angeles_Rams':
#             print(lst)
            # if and 1949 clev brnws
            # if Los_Angeles_Rams & 1936
        
        
        if attch_next_row == True:
            # The preceding row is verified to be prior to 1933
            # and therefore will be extended to the previous row
            attch_next_row = False
            new_lsts[-1].extend(['',''])
            new_lsts[-1].extend(lst)
        elif verifyrowdata(lst) == True:
            # This row has been verified to have real data
            if (int(lst[0][0:4]) < 1933) or (logic_exception == True and int(lst[0][0:4]) == logic_exception_year[team]):
                # This row has been verified to be prior to 1933
                attch_next_row = True
            new_lsts.append(lst)
        else:
            # This row contains no useful data
            attch_next_row = False
    return new_lsts

def buildlistofdicts(lsts, key_dict, starting_list_index=2, additional_values_dict = {}):
    # Assumes the first two lists contain poorly formatted headers
    # lsts = contains the list of lists that will be converted to a list of dictionarires
    # keys_dict = keys: strings that will be used to create the keys in the resulting dictist
        # values: the index numbers to access the elements in the sublist that will be the values in the dictlst
    dictlst = []
    for lst in lsts[starting_list_index:]:
        
        if additional_values_dict['Team'] == 'San_Francisco_49ers':
            print(lst) 
        
        temp_dict = {}
        for key, index in key_dict.items(): # New_York_Giants San_Francisco_49ers - AttributeError: 'NoneType' object has no attribute 'items'
            
            # handling special cases
            if key == 'Post_Season_Results':
                
                if index < len(lst): 
                    if lst[index] == "":
                        temp_dict[key] = 'Did Not Qualify'
                    else:
                        temp_dict[key] = ",".join(lst[index:])
                    
                else:
                    temp_dict[key] = 'Did Not Qualify'
            
            else:
                temp_dict[key] = lst[index]
        
        # Add additional values
        for key, value in additional_values_dict.items():
            temp_dict[key] = value
                
        dictlst.append(temp_dict)
        
    return dictlst

def count_playoffwins(playoffdata):
    win_string = 'won'
    playoffdata_lowercase = playoffdata.lower()
    return len(playoffdata_lowercase.split(win_string)) - 1
 
def count_playofflosses(playoffdata):
    loss_string = 'lost'
    playoffdata_lowercase = playoffdata.lower()
    return len(playoffdata_lowercase.split(loss_string)) - 1
    
url_base = 'https://en.wikipedia.org'
url_dict = {'Chicago_Bears': "/wiki/List_of_Chicago_Bears_seasons"}                        
url = url_base + url_dict['Chicago_Bears']
response = requests.get(url)

content = response.content

# Initialize the parser, and pass in the content we grabbed earlier.
# I'm guessing that the parser is deterimnie from the DOCTYPE
parser = BeautifulSoup(content, 'html.parser')

# Get the list of urls from the NFL team seasons lists found @ = "https://en.wikipedia.org/wiki/List_of_Chicago_Bears_seasons"
a_items = parser.find_all('a')

# compile regular expression pattern to find the team season urls
url_string_pattern = re.compile("/wiki/List_of_(.*)_seasons")

for a_item in a_items:
    
    try:
        result = url_string_pattern.search(a_item['href'])
        if result != None:
            text_value = str(a_item.text).replace(" ", "_")
            group1_value = result.group(1)
            if text_value == group1_value:
                url_dict[text_value] = str(a_item['href'])
        
    except KeyError:
        pass
    
# pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)
# pp.pprint(url_dict)

# iterate through the url_dict and for each teams Season by Season table
# Get the win loss data

team_data_lst = []
team_data_dict = {}

season_pattern = re.compile('(.*)season(.*)')
team_pattern = re.compile('(.*)team(.*)')
league_pattern = re.compile('(.*)league(.*)')
conference_pattern = re.compile('(.*)conference(.*)')

# url_dict.pop('Cleveland_Browns', None)  # IndexError: list index out of range (line 113)
# url_dict.pop('New_York_Giants', None) # AttributeError: 'NoneType' object has no attribute 'items' (line 98)
url_dict.pop('Detroit_Lions', None) # Exception: Unexpected Data Formatting: The string = "Season" was not found in the home value. (line 232)
# url_dict.pop('Los_Angeles_Rams', None) # IndexError: list index out of range (line 113)
# url_dict.pop('San_Francisco_49ers', None) # AttributeError: 'NoneType' object has no attribute 'items' (line 98)

for team_name, team_url in url_dict.items():
    
    # scrape the team win loss data
    url = url_base + team_url
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    
    print(team_name + ": " + url)
    
    # Get the win loss data from the Season by Season table
    tabs = parser.find_all('table')
    season_record_row_strings = None
    
    x = 0
    
    for tab in tabs:
        
        x += 1
        
        # Iterates through each table looking for the "season-by-season" win loss data table
        # The table with "Season", "Team", "League", & "Conference" in the 1st 10 elements is the "season-by-season" win loss data table
        temp = tab.text.split('\n')
        
        if team_name == 'Detroit_Lions':
            print(temp)
        
        # Check for primer strings
        season_found, team_found, league_found, conference_found = False, False, False, False
        
        for value in temp[0:20]:
            
            if team_name == 'Detroit_Lions' and x == 2:
                print(value)
            
            if season_pattern.search(value.lower()) != None:
                season_found = True
            elif team_pattern.search(value.lower()) != None:
                team_found = True
            elif league_pattern.search(value.lower()) != None:
                league_found = True
            elif conference_pattern.search(value.lower()) != None:
                conference_found = True
     
#         if 'Season' in temp[0:10] and 'Team' in temp[0:10] and 'League' in temp[0:10] and 'Conference' in temp[0:10]:
            # each table row is delimited by 3 new line characters
        if season_found and team_found and league_found and conference_found:
            season_record_row_strings = tab.text.split('\n\n\n')
#             if team_name == 'New_York_Giants' or team_name == 'San_Francisco_49ers':
#                 for row in season_record_row_strings:
#                     print(row.split('\n'))
    
    # If the season is not found or formatted differently then raise an exception        
    if season_record_row_strings == None:
        print('season_found:', season_found)
        print('team_found:', team_found)
        print('league_found:', league_found)
        print('conference_found:', conference_found)
        raise Exception('Unexpected Data Formatting: The string = "Season" was not found in the home value.')
        # Detroit_Lions
            
    # Structre data: list if libraries that can be converted into a pd DataFrame
        # 1) Each row terminates with '\n\n\n' (with few exceptions)
        # 2) Within each row each value is separated by a '\n'
    
    # Splits the primary string into a list of strings each list item are the values for a given row
    # Iterate through each row string and split into individual values
    season_record_lsts = [row_str.split('\n') for row_str in season_record_row_strings]
       
    # Clean up the data set
    # Removing leading '' elements
    season_record_lsts[:] = [remove_leading_empties(sublist) for sublist in season_record_lsts]
    
    
    if team_name == "San_Francisco_49ers":
        for lst in season_record_lsts:
            print(lst)
    
    
    # All rows of a single element contain no win loss data and are thus removed
    season_record_lsts[:] = [sublist for sublist in season_record_lsts if len(sublist) > 1] 
    # All rows whose 0th & 1st elements are not the same 4 digit integer are culled
    cleaned_season_record_lsts = cleanlsts(season_record_lsts, team=team_name)
    
    # Restructure data into list of dictionaries
    # each dictionary is a row of data where the key = header and value = value
    
#     if team_name == 'New_York_Giants' or team_name == 'San_Francisco_49ers':
#         print(cleaned_season_record_lsts[:1])
    
    key_dict = determineheaderstyle(cleaned_season_record_lsts, team_name)
    seasons_lst_of_dicts = buildlistofdicts(cleaned_season_record_lsts, key_dict, additional_values_dict={'Team': team_name, 'url': url})
    # Create DataFrame for easy data manuplation
    season_df = pd.DataFrame(seasons_lst_of_dicts)
    
    # Parce playoff data to get playoff wins losses, & Games_Played
    season_df['Wins_Pl'] = season_df['Post_Season_Results'].apply(count_playoffwins)
    season_df['Losses_Pl'] = season_df['Post_Season_Results'].apply(count_playofflosses)
    season_df['Games_Played'] = season_df['Wins_Pl'] + season_df['Losses_Pl']
    
    # print(season_df[['Year','Wins_Pl','Losses_Pl', 'Games_Played', 'Post_Season_Results']][season_df['Games_Played'] > 0])
    
    team_data_lst.append(season_df)
    team_data_dict[team_name] = season_df
    
combined_team_data = team_data_lst[0].append(team_data_lst[1:])
FileName = os.path.join(os.getcwd(),'NFL_SeasonalWins_latin.csv')
combined_team_data.to_csv(FileName, encoding='utf-8')
