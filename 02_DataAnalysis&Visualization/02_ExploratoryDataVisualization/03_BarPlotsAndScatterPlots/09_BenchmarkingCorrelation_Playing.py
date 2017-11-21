import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('fandango_scores.csv')

# The Axes.bar() method has 2 required parameters, left and height. We use the left
# parameter to specify the x coordinates of the left sides of the bar (marked in
# blue on the above image). We use the height parameter to specify the height of each
# bar. Both of these parameters accept a list-like object.
fig = plt.figure(figsize=(18,9))
# ax1 = fig.add_subplot(3,1,1)
# ax2 = fig.add_subplot(3,1,2)
# ax3 = fig.add_subplot(3,1,3)
# ax = [ax1, ax2, ax3]

color_codes = ['red', 'blue', 'green']
x_series = [reviews['Fandango_Ratingvalue'], reviews['Fandango_Ratingvalue'], reviews['Fandango_Ratingvalue']]

y_series = [reviews['RT_user_norm'], reviews['Metacritic_user_nom'], reviews['IMDB_norm']]
data_labels = ['Rotten Tomatoes', 'Metacritic', 'IMDB']


for plot in range(0,3):
	
	plt.scatter(x_series[plot], y_series[plot], color=color_codes[plot], label=data_labels[plot], marker='*')

plt.legend(loc='upper left')
#plt.set_ylabel('Rating')
#plt.set_xlabel('Fandango')
#plt.title('Rating vs. Fandango')	
#plt.set_xlim(0, 5)
#plt.set_ylim(0, 5)

plt.show()