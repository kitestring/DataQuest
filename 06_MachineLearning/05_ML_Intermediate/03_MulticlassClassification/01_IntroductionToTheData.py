# origin -- Integer and Categorical. 1: North America, 2: Europe, 3: Asia.

import pandas as pd

cars = pd.read_csv('auto.csv')
print(cars.info())

unique_cylinders = cars['cylinders'].unique()
print('\nunique_cylinders:', unique_cylinders)

unique_model_year = cars['year'].unique()
print('\nunique_model_year:', unique_model_year)

unique_regions = cars['origin'].unique()
print('\nunique_regions:', unique_regions)


# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 392 entries, 0 to 391
# Data columns (total 10 columns):
# Unnamed: 0      392 non-null int64
# mpg             392 non-null float64
# cylinders       392 non-null int64
# displacement    392 non-null float64
# horsepower      392 non-null float64
# weight          392 non-null float64
# acceleration    392 non-null float64
# year            392 non-null int64
# origin          392 non-null int64
# car_name        392 non-null object
# dtypes: float64(5), int64(4), object(1)
# memory usage: 30.7+ KB
# None

# unique_cylinders: [8 4 6 3 5]
# unique_model_year: [70 71 72 73 74 75 76 77 78 79 80 81 82]
# unique_regions: [1 3 2]