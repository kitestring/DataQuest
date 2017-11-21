# order the charts by decreasing ending gender
# gap. We've populated the list stem_cats with
# the six STEM degree categories. In the next
# step, we'll explore how we can replace the legend

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,7):
    ax = fig.add_subplot(1,7,sp+1)
    if sp < 6:
        ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
        ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
        
        ax.set_xlim(1968, 2011)
        ax.set_ylim(0,100)
        ax.set_title(stem_cats[sp])   

        for key,spine in ax.spines.items():
            spine.set_visible(False)
        
            ax.tick_params(bottom="off", top="off", left="off", right="off")
        
        if sp == 0:
            ax.text(2005, 87, "Men")
            ax.text(2002, 8, "Women")
        elif sp == 5:
            ax.text(2005, 62, "Men")
            ax.text(2005, 35, "Women")
    else:
        ax.plot() 
        
    
        
plt.legend(loc='upper right')
plt.show()