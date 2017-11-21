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

for key, df in data.items():
    print('*****')
    print(key)
    print(df.head(5))
    print('*****\n\n')