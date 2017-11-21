# Write a function that:
# Takes in a string
# Uses the regular expression above to extract the coordinates
# Uses string manipulation functions to pull out the latitude
# Returns the latitude
# Use the df.apply() method to apply the function across the Location 1 column of hs_directory. Assign the result to the lat column of hs_directory.
# Display the first few rows of hs_directory to verify the results.


import re
import pandas as pd


def padded_csd(row):
    return str(row['CSD']).zfill(2)

def extract_lat_long(row):
    found_string = re.findall("\(.+\)", row['Location 1'])
    parced_coordinates = found_string[0].split(',')
    lat = parced_coordinates[0].replace('(','')
    return lat

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

data['hs_directory']['lat'] = data['hs_directory'].apply(extract_lat_long, axis=1)

print(data['hs_directory'].head())