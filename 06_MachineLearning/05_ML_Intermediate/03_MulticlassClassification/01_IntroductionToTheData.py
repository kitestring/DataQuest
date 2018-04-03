import pandas as pd

cars = pd.read_csv('cars.csv')

unique_regions = cars['origin'].unique()
print('unique_regions:', unique_regions)

# unique_regions: [1 3 2]