# Copy the dbn column in hs_directory into a new column called DBN.
# Create a new column called padded_csd in the class_size data set.
# Use the pandas.DataFrame.apply() method along with a custom function to generate this column.
# Make sure to apply the function along the data["class_size"]["CSD"] column.
# Use the addition operator (+) along with the padded_csd and SCHOOL CODE columns of class_size, then assign the result to the DBN column of class_size.
# Display the first few rows of class_size to double check the DBN column.


import pandas as pd

def padded_csd(row):
    return str(row['CSD']).zfill(2)

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
#     Note dataquest is using linux or ios thus it will utilize a forward slash not a back slash
#     data[data_file[:-4]] = pd.read_csv('schools/' + data_file)

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
print(data['class_size'].head(3))

# Create Table Name column
# tableName_series = df.apply(self.get_table_name, axis=1)
# df['TableName'] = tableName_series