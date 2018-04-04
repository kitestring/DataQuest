import numpy as np
import pandas as pd

# read csv files
cars = pd.read_csv('auto.csv')

# create dummy variables for the categorical variables
dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

# drop the dummy originating columns
cars = cars.drop(['cylinders', 'year'], axis=1)


# Split the shuffled_cars Dataframe into 2 Dataframes: train and test.
# Assign the first 70% of the shuffled_cars to train.
# Assign the last 30% of the shuffled_cars to test.
np.random.seed(1)
shuffled_index = np.random.permutation(cars.index)
shuffled_cars = cars.reindex(shuffled_index)

seventy_percent = round(len(shuffled_cars) * 0.7)

train = shuffled_cars.iloc[0:seventy_percent]
test = shuffled_cars.iloc[seventy_percent:]

