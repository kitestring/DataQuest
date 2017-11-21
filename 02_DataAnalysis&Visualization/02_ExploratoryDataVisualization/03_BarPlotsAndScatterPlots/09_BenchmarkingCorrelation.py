import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('fandango_scores.csv')

# The Axes.bar() method has 2 required parameters, left and height. We use the left
# parameter to specify the x coordinates of the left sides of the bar (marked in
# blue on the above image). We use the height parameter to specify the height of each
# bar. Both of these parameters accept a list-like object.
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax = [ax1, ax2, ax3]

x_series = [reviews['Fandango_Ratingvalue'], reviews['Fandango_Ratingvalue'], reviews['Fandango_Ratingvalue']]
x_labels = ['Fandango', 'Fandango', 'Fandango']

y_series = [reviews['RT_user_norm'], reviews['Metacritic_user_nom'], reviews['IMDB_norm']]
y_labels = ['Rotten Tomatoes', 'Metacritic', 'IMDB']


for n, axis in enumerate(ax):
	
	axis.scatter(x_series[n], y_series[n])
	axis.set_ylabel(y_labels[n])
	axis.set_xlabel(x_labels[n])
	axis.set_xlim(0, 5)
	axis.set_ylim(0, 5)

plt.show()