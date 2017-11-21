# Display the first five rows of the SAT scores data.
# Use the key sat_results to access the SAT scores dataframe stored in the dictionary data.
# Use the pandas.DataFrame.head() method along with the print() function to display the first five rows of the dataframe.

# NOte DBN = district borough number

import pandas as pd

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

print(data['sat_results'].head(5))