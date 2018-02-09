import pandas as pd

income = pd.read_csv('income.csv')

print('pd.crosstab creates an observed frequency table\nhandy...\n')
table = pd.crosstab(income["sex"], [income["race"]])
print(table)

print("Here's how to get the values out if you're so inclined")

observed_Amer_Indian_Eskimo_Females = table.loc[' Female'][' Amer-Indian-Eskimo']
observed_Asian_Pac_Islander_Females = table.loc[' Female'][' Asian-Pac-Islander']
observed_Black_Females = table.loc[' Female'][' Black']
observed_Other_Females = table.loc[' Female'][' Other']
observed_White_Females = table.loc[' Female'][' White']

observed_Amer_Indian_Eskimo_Males = table.loc[' Male'][' Amer-Indian-Eskimo']
observed_Asian_Pac_Islander_Males = table.loc[' Male'][' Asian-Pac-Islander']
observed_Black_Males = table.loc[' Male'][' Black']
observed_Other_Males = table.loc[' Male'][' Other']
observed_White_Males = table.loc[' Male'][' White']