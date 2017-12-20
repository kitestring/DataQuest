import os
import pprint
import re
from jsonAPI import JSON_Tools
from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrapeESPN_Kicking(url, optional_values = {}):
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    tables = parser.select('table')
    
    list_of_dicts = []
    headers = []
    
    
    for table in tables:
        # Iterate through each table
        
        # Get all the rows from a given table
        rows = table.select('tr')
        
        for row_index, row in enumerate(rows):
            # Iterate through each row
            
            # Get each column within the row
            columns = row.select('td')
            
            # The first row is the headers
            if row_index > 0:
                list_of_dicts.append({})
                r = row_index-2
                # add optional values to dict
                for key, value in optional_values.items():
                    list_of_dicts[r][key] = value 
            
            for column_index, column in enumerate(columns):
                # Iterate through each column value
                if row_index == 1:
                    # First pass through get the headers which will be used as keys in the dict
                    # The string appendages deals with grouped columns
                    if column_index <= 1:
                        headers.append(column.text)
                    elif column_index >= 2 and column_index <= 10:
                        headers.append(column.text + '_FGOALS')
                    elif column_index >= 7:
                        headers.append(column.text + '_EPOINTS')
                     
                elif row_index >= 2:
                    # Every other pass through assign a value to each key in the dictionary 
                    # that has just been appended to the list_of_dicts
                    headers[column_index]
                    list_of_dicts[r][headers[column_index]] = column.text
                    
    return list_of_dicts

def scrapeESPN_Returns(url, optional_values = {}):
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    tables = parser.select('table')
    
    list_of_dicts = []
    headers = []
    
    
    for table in tables:
        # Iterate through each table
        
        # Get all the rows from a given table
        rows = table.select('tr')
        
        for row_index, row in enumerate(rows):
            # Iterate through each row
            
            # Get each column within the row
            columns = row.select('td')
            
            # The first row is the headers
            if row_index > 0:
                list_of_dicts.append({})
                r = row_index-2
                # add optional values to dict
                for key, value in optional_values.items():
                    list_of_dicts[r][key] = value 
            
            for column_index, column in enumerate(columns):
                # Iterate through each column value
                if row_index == 1:
                    # First pass through get the headers which will be used as keys in the dict
                    # The string appendages deals with grouped columns
                    if column_index <= 1:
                        headers.append(column.text)
                    elif column_index >= 2 and column_index <= 6:
                        headers.append(column.text + '_KICKOFFS')
                    elif column_index >= 7:
                        headers.append(column.text + '_PUNTS')
                     
                elif row_index >= 2:
                    # Every other pass through assign a value to each key in the dictionary 
                    # that has just been appended to the list_of_dicts
                    headers[column_index]
                    list_of_dicts[r][headers[column_index]] = column.text
                    
    return list_of_dicts

def scrapeESPN_Down_Penalties(url, optional_values = {}):
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    tables = parser.select('table')
    
    list_of_dicts = []
    headers = []
    
    
    for table in tables:
        # Iterate through each table
        
        # Get all the rows from a given table
        rows = table.select('tr')
        
        for row_index, row in enumerate(rows):
            # Iterate through each row
            
            # Get each column within the row
            columns = row.select('td')
            
            # The first row is the headers
            if row_index > 0:
                list_of_dicts.append({})
                r = row_index-2
                # add optional values to dict
                for key, value in optional_values.items():
                    list_of_dicts[r][key] = value 
            
            for column_index, column in enumerate(columns): 
                # Iterate through each column value
                if row_index == 1:
                    # First pass through get the headers which will be used as keys in the dict
                    # The string appendages deals with grouped columns
                    if column_index <= 1:
                        headers.append(column.text)
                    elif column_index >= 2 and column_index <= 5:
                        headers.append(column.text + '_1Dn')
                    elif column_index >= 6 and column_index <= 8:
                        headers.append(column.text + '_3Dn')
                    elif column_index >= 9 and column_index <= 11:
                        headers.append(column.text + '_4Dn')
                    elif column_index >= 12:
                        headers.append(column.text + '_PENALTIES')
                     
                elif row_index >= 2:
                    # Every other pass through assign a value to each key in the dictionary 
                    # that has just been appended to the list_of_dicts
                    headers[column_index]
                    list_of_dicts[r][headers[column_index]] = column.text
                
    return list_of_dicts

def scrapeESPN_Turnovers(url, optional_values = {}):
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    tables = parser.select('table')
    
    list_of_dicts = []
    headers = []
    
    
    for table in tables:
        # Iterate through each table
        
        # Get all the rows from a given table
        rows = table.select('tr')
        
        for row_index, row in enumerate(rows):
            # Iterate through each row
            
            # Get each column within the row
            columns = row.select('td')
            
            # The first row is the headers
            if row_index > 0:
                list_of_dicts.append({})
                r = row_index-2
                # add optional values to dict
                for key, value in optional_values.items():
                    list_of_dicts[r][key] = value 
            for column_index, column in enumerate(columns):
                
                # Iterate through each column value
                if row_index == 1:
                    # First pass through get the headers which will be used as keys in the dict
                    # The string appendages deals with grouped columns
                    if column_index <= 1:
                        headers.append(column.text)
                    elif column_index >= 2 and column_index <= 4:
                        headers.append(column.text + '_TACK')
                    elif column_index >= 5 and column_index <= 6:
                        headers.append(column.text + '_SACK')
                    elif column_index >= 7 and column_index <= 11:
                        headers.append(column.text + '_INT')
                    elif column_index >= 12:
                        headers.append(column.text + '_FUM')
                    
                elif row_index >= 2:
                    # Every other pass through assign a value to each key in the dictionary 
                    # that has just been appended to the list_of_dicts
                    headers[column_index]
                    list_of_dicts[r][headers[column_index]] = column.text
                
    return list_of_dicts

def scrapeESPN_Totals(url, optional_values = {}):
    response = requests.get(url)
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    tables = parser.select('table')
    
    list_of_dicts = []
    headers = []
    
    
    for table in tables:
        # Iterate through each table
        
        # Get all the rows from a given table
        rows = table.select('tr')
        
        for row_index, row in enumerate(rows):
            # Iterate through each row
            
            # Get each column within the row
            columns = row.select('td')
            
            # The first row is the headers
            if row_index > 0:
                list_of_dicts.append({})
                r = row_index-1
                # add optional values to dict
                for key, value in optional_values.items():
                    list_of_dicts[r][key] = value 
            
            for column_index, column in enumerate(columns):
                # Iterate through each column value
                if row_index == 0:
                    # First pass through get the headers which will be used as keys in the dict
                    headers.append(column.text)
                else:
                    # Every other pass through assign a value to each key in the dictionary 
                    # that has just been appended to the list_of_dicts
                    list_of_dicts[r][headers[column_index]] = column.text
                    
    return list_of_dicts

# ***urls***
# Defense: 
    # Total defense (yards & points given up)
        # http://www.espn.com/nfl/statistics/team/_/stat/total/position/defense/year/2016
    # Tackles, sacks, turnovers & TD's (taken)
        # http://www.espn.com/nfl/statistics/team/_/stat/defense/year/2016
    # Penalties & down statistics
        # http://www.espn.com/nfl/statistics/team/_/stat/downs/position/defense/year/2016
        

# Offense:  2002 - 2016 both regular season and post season
    # Penalties & down statistics
        # http://www.espn.com/nfl/statistics/team/_/stat/downs/year/2016
    # Total offense
        # http://www.espn.com/nfl/statistics/team/_/stat/total/year/2016
     # Tackles, sacks, and turnovers given up
        # http://www.espn.com/nfl/statistics/team/_/stat/defense/position/defense/year/2016
    
# Special teams: 2002 - 2016 both regular season and post season
    # own return
        # http://www.espn.com/nfl/statistics/team/_/stat/returning/year/2016 
    # opponent returning
        # http://www.espn.com/nfl/statistics/team/_/stat/returning/position/defense/year/2016
    # Kicking (field goals & extra points)
        # http://www.espn.com/nfl/statistics/team/_/stat/kicking/year/2016

data_sets = {
    'def_tot_url': {'url': 'http://www.espn.com/nfl/statistics/team/_/stat/total/position/defense/year/', 'custom_columns': {'phase': 'Defense'}}, # rush, passing, total yards and points allowed
    'def_turnovers_url': {'url': 'http://www.espn.com/nfl/statistics/team/_/stat/defense/year/', 'custom_columns': {'phase': 'Defense'}}, # forced turnovers, years and points off forced turnovers
    'def_down_penalty_url': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/downs/position/defense/year/', 'custom_columns': {'phase': 'Defense'}}, # yards and points given up by down and defensive Penalties
    'off_tot_url': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/total/year/', 'custom_columns': {'phase': 'Offense'}}, # rush, passing, total yards and points gained
    'off_turnovers_url': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/defense/position/defense/year/', 'custom_columns': {'phase': 'Offense'}}, # forced turnovers, years and points off forced turnovers
    'off_down_penalty_url': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/downs/year/', 'custom_columns': {'phase': 'Offense'}}, # yards and points obtained by down and offensive Penalties
    'st_own_return': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/returning/year/', 'custom_columns': {'phase': 'Off_STeams'}}, # Teams own return yards / points
    'st_opponent_return': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/returning/position/defense/year/', 'custom_columns': {'phase': 'Def_STeams'}}, # Opponents return yards / points
    'st_kicking': {'url':'http://www.espn.com/nfl/statistics/team/_/stat/kicking/year/', 'custom_columns': {'phase': 'STeams'}} # Field goal and extra point kicking
    }

years = [str(y) for y in range(2002,2017)]
JSON_Tools = JSON_Tools()
nfl_stats = {} 

for data_name, data_set in data_sets.items():
    
    print(data_name)
    
    list_of_dicts = []
    
    for year in years:
        
        url = data_set['url'] + year
        
        if data_name == 'def_turnovers_url' or data_name == 'off_turnovers_url':
            list_of_dicts.extend(scrapeESPN_Turnovers(url, optional_values={'year': year, 'phase': data_set['custom_columns']['phase'], 'url': url}))
            
        elif data_name == 'def_down_penalty_url' or data_name == 'off_down_penalty_url':
            list_of_dicts.extend(scrapeESPN_Down_Penalties(url, optional_values={'year': year, 'phase': data_set['custom_columns']['phase'], 'url': url}))
            
        elif data_name == 'def_tot_url' or data_name == 'off_tot_url':
            list_of_dicts.extend(scrapeESPN_Totals(url, optional_values={'year': year, 'phase': data_set['custom_columns']['phase'], 'url': url}))
            
        elif data_name == 'st_own_return' or data_name == 'st_opponent_return':
            list_of_dicts.extend(scrapeESPN_Returns(url, optional_values={'year': year, 'phase': data_set['custom_columns']['phase'], 'url': url}))
            
        elif data_name == 'st_kicking':
            list_of_dicts.extend(scrapeESPN_Kicking(url, optional_values={'year': year, 'phase': data_set['custom_columns']['phase'], 'url': url}))
     
    # Create a df and print it to csv file   
    data_set_df = pd.DataFrame(list_of_dicts)
    FileName = os.path.join(os.getcwd(),data_name[:-4] + '.csv')
    data_set_df.to_csv(FileName, encoding='utf-8')
    
    nfl_stats[data_name] = list_of_dicts
    
    
FileName = os.path.join(os.getcwd(),'NFL_stats.json')
JSON_Tools.dump_Data_To_File(FileName, nfl_stats=nfl_stats)