import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

# This function returns the hundredth item from a series
def hundredth_row(column):
    # Extract the hundredth item
    hundredth_item = column.iloc[99]
    return hundredth_item

# Return the hundredth item from each column
hundredth_row_var = titanic_survival.apply(hundredth_row)
print(hundredth_row_var)
raw_input("\nPress Enter To Continue\n")

# this will return the save series
print(titanic_survival.iloc[99,:])

