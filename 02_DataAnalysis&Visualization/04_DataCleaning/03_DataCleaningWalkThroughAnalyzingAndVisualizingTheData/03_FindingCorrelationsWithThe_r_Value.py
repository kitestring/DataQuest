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

def left2(row):
    return str(row['DBN'])[0:2]

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

# for data_file in data_files:
#     data[data_file[:-4]] = pd.read_csv('schools\\' + data_file)
# 
# all_survey = pd.read_csv('schools\\' + 'survey_all.txt', delimiter="\t", encoding="windows-1252")
# d75_survey = pd.read_csv('schools\\' + 'survey_d75.txt', delimiter="\t", encoding="windows-1252")

for data_file in data_files:
    data[data_file[:-4]] = pd.read_csv('schools/' + data_file)
 
all_survey = pd.read_csv('schools/' + 'survey_all.txt', delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv('schools/' + 'survey_d75.txt', delimiter="\t", encoding="windows-1252")

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

# Condensing The Graduation Data Set

# Filter graduation, only selecting rows where the Cohort column equals 2006.
# Filter graduation, only selecting rows where the Demographic column equals Total Cohort.
# Display the first few rows of data["graduation"] to verify that everything worked properly.
data["graduation"] = data['graduation'][(data['graduation']['Cohort'] == '2006') & (data['graduation']['Demographic'] == 'Total Cohort')]


# Converting AP Test Scores


# Convert each of the following columns in ap_2010 to numeric values using the pandas.to_numeric() function with the keyword argument errors="coerce".
    # AP Test Takers
    # Total Exams Taken
    # Number of Exams with scores 3 4 or 5
# Display the first few rows of ap_2010 to confirm.

# data['ap_2010'] = 
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col], errors="coerce")
    


# Performing The Left Joins

# Use the pandas pandas.DataFrame.merge() method to merge the ap_2010 data set into combined.
    # Make sure to specify how="left" as a keyword argument to indicate the correct join type.
    # Make sure to assign the result of the merge operation back to combined.
# Use the pandas df.merge() method to merge the graduation data set into combined.
    # Make sure to specify how="left" as a keyword argument to get the correct join type.
    # Make sure to assign the result of the merge operation back to combined.
# Display the first few rows of combined to verify that the correct operations occurred.
# Use the pandas.DataFrame.shape() attribute to display the shape of the dataframe and see how many rows now exist.

data_frames = [
    "sat_results",
    "ap_2010",
    "graduation",
    "class_size",
    "demographics",
    'survey',
    "hs_directory"
]

combined = data[data_frames[0]]

for data_frame in data_frames[1:3]:
    combined = combined.merge(data[data_frame], on='DBN', how="left")
    
for data_frame in data_frames[3:7]:
    combined = combined.merge(data[data_frame], on='DBN', how="inner")
    
# Calculate the means of all of the columns in combined using the pandas.DataFrame.mean() method.
# Fill in any missing values in combined with the means of the respective columns using the pandas.DataFrame.fillna() method.
# Fill in any remaining missing values in combined with 0 using the df.fillna() method.
# Display the first few rows of combined to verify that the correct operations occurred.

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)




# Write a function that extracts the first two characters of a string and returns them.
# Apply the function to the DBN column of combined, and assign the result to the school_dist column of combined.
# Display the first few items in the school_dist column of combined to verify the results.

combined['school_dist'] = combined.apply(left2, axis=1)



# Use the pandas.DataFrame.corr() method on the combined dataframe to find all possible correlations. Assign the result to correlations.
# Filter correlations so that it only shows correlations for the column sat_score.
# Display all of the rows in correlations and look them over.

correlations = combined.corr()
correlations = correlations["sat_score"]
print(correlations)