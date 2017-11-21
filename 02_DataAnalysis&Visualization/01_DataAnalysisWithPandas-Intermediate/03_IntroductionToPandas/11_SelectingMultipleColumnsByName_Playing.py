import pandas

food_info = pandas.read_csv('food_info.csv')

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

# Skipping the assignment.
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

print(zinc_copper)