import pandas as pd

income = pd.read_csv('us_income.csv')
print(income.head())
print('')
 
columns = income.columns
 
for c in columns:
    print(c)

print(income['median_income'].min())
    
lowest_income_county = income['county'][income['median_income'].min() == income['median_income']]
print('\nlowest_income_county:', lowest_income_county)

high_pop_county = income[income['pop_over_25'] > 500000]
lowest_income_high_pop_county = high_pop_county['county'][high_pop_county['median_income'].min() == high_pop_county['median_income']]

print('\nlowest_income_high_pop_county:', lowest_income_high_pop_county)