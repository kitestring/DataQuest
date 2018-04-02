import pandas as pd
import matplotlib.pyplot as plt

admissions = pd.read_csv('admissions.csv')

fig = plt.figure()
plt.scatter(admissions['gpa'],admissions['admit'])

plt.show()