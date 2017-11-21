import pandas

food_info = pandas.read_csv('food_info.csv')

# DataFrame containing the rows at index 3, 4, 5, and 6 returned.
print(food_info.loc[3:6])

# DataFrame containing the rows at index 2, 5, and 10 returned. Either of the following work.
# Method 1
two_five_ten = [2,5,10] 
print(food_info.loc[two_five_ten])

# Method 2
print(food_info.loc[[2,5,10]])