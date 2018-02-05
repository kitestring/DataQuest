import pandas as pd
bikes = pd.read_csv("bike_rental_day.csv")

days_over_threshold = bikes[bikes["cnt"] > 4000].shape[0]
total_days = bikes.shape[0]

probability_over_4000 = days_over_threshold / total_days
print(probability_over_4000)

