# Filter demographics, only selecting rows in data["demographics"] where schoolyear is 20112012.
    # schoolyear is actually an integer, so be careful about how you perform your comparison.
# Display the first few rows of data["demographics"] to verify that the filtering worked.

import re
import pandas as pd


def padded_csd(row):
    return str(row['CSD']).zfill(2)

def find_coordinates_lst(str_location):
    found_string = re.findall("\(.+\)", str_location)
    return found_string[0].split(',')

def extract_lat(row):
    coordinates_lst = find_coordinates_lst(row['Location 1'])
    return coordinates_lst[0].replace('(','')

def extract_lon(row):
    coordinates_lst = find_coordinates_lst(row['Location 1'])
    return coordinates_lst[1].replace(')','')

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for data_file in data_files:
    data[data_file[:-4]] = pd.read_csv('schools\\' + data_file)

all_survey = pd.read_csv('schools\\' + 'survey_all.txt', delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv('schools\\' + 'survey_d75.txt', delimiter="\t", encoding="windows-1252")

# for data_file in data_files:
#     data[data_file[:-4]] = pd.read_csv('schools/' + data_file)
# 
# all_survey = pd.read_csv('schools/' + 'survey_all.txt', delimiter="\t", encoding="windows-1252")
# d75_survey = pd.read_csv('schools/' + 'survey_d75.txt', delimiter="\t", encoding="windows-1252")

survey = pd.concat([all_survey, d75_survey], axis=0)

cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey["DBN"] = survey["dbn"]
survey = survey.loc[:,cols]
data["survey"] = survey

data['hs_directory']['DBN'] = data['hs_directory']['dbn']

data['class_size']['padded_csd'] = data['class_size'].apply(padded_csd, axis=1)
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']

data['sat_results']['SAT Math Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Math Avg. Score'], errors='coerce')
data['sat_results']['SAT Critical Reading Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Critical Reading Avg. Score'], errors='coerce')
data['sat_results']['SAT Writing Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Writing Avg. Score'], errors='coerce')

data['sat_results']['sat_score'] = data['sat_results']['SAT Math Avg. Score'] + data['sat_results']['SAT Critical Reading Avg. Score'] + data['sat_results']['SAT Writing Avg. Score']

data['hs_directory']['lat'] = data['hs_directory'].apply(extract_lat, axis=1)
data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')

data['hs_directory']['lon'] = data['hs_directory'].apply(extract_lon, axis=1)
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')

# Condensing the Class Size Data Set by removing duplicate DBN entries
class_size = data["class_size"]
class_size = class_size[class_size['GRADE '] == '09-12']
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']

# Averaging SAT scores to further condense and remove duplicate DBN entries

# Find the average values for each column associated with each DBN in class_size.
    # Use the pandas.DataFrame.groupby() method to group class_size by DBN.
    # Use the agg() method on the resulting pandas.core.groupby object, along with the numpy.mean() function as an argument, to calculate the average of each group.
    # Assign the result back to class_size.
    
class_size = class_size.groupby('DBN').mean()

# Reset the index to make DBN a column again.
    # Use the pandas.DataFrame.reset_index() method, along with the keyword argument inplace=True.

class_size.reset_index(inplace=True)   

# Assign class_size back to the class_size key of the data dictionary.
data["class_size"] = class_size

# Filter demographics, only selecting rows in data["demographics"] where schoolyear is 20112012.
    # schoolyear is actually an integer, so be careful about how you perform your comparison.
data['demographics'] = data['demographics'][data['demographics']['schoolyear'] == 20112012]

# Display the first few rows of data["demographics"] to verify that the filtering worked.
print(data['demographics'].head())