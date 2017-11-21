import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('fandango_scores.csv')

fig, ax = plt.subplots()
ax.hist(reviews['Fandango_Ratingvalue'], range=(0, 5))
plt.show()