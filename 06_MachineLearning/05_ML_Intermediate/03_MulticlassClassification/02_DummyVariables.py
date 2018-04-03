import pandas as pd

# read csv files
cars = pd.read_csv('cars.csv')

# create dummy variables for the categorical variables
dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

# drop the dummy originating columns
cars = cars.drop(['cylinders', 'year'], axis=1)

print(cars.head(5))