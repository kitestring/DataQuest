import pandas as pd
import numpy as np

fandango = pd.read_csv('fandango_score_comparison.csv')

# Use the pandas dataframe method set_index to assign the FILM
# column as the custom index for the dataframe. Also, specify
# that we don't want to drop the FILM column from the dataframe.
# We want to keep the original dataframe, so assign the new one to fandango_films.

fandango_films = fandango.set_index('FILM', drop=False)

# returns the data types as a Series where the fandango_films headers is the index & the correspoinding type is the value
types = fandango_films.dtypes

# filter data types to just floats, index attributes returns just column names
# types.values == 'float64' (returns a boolean series)
# returns the index values that have a 'float64' type which correspond to the columns in the fandango_films dataframe
float_columns = types[types.values == 'float64'].index

# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# Use the apply() method to calculate the average of each movie's values for RT_user_norm and
# Metacritic_user_nom, and assign the result to the variable rt_mt_means.
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)

# Display the first five values in rt_mt_means.
print(rt_mt_means[0:5])