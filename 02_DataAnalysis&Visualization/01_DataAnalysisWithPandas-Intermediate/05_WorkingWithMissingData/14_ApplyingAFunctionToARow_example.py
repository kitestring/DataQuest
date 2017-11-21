import pandas as pd

# This function checks the passenger class 
def which_class(row):
    pclass = row['pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    else:
        return "Third Class"

titanic_survival = pd.read_csv('titanic_survival.csv')
		
# Iterates through each row and checks the passenger class
classes = titanic_survival.apply(which_class, axis=1)
print(classes)