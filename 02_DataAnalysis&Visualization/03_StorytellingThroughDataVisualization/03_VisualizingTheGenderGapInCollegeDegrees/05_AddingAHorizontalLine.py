import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(16, 16))

# Adds the stem majors plots to the figure object
for index, sp in enumerate(range(0,16,3)):
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[index])
    ax.set_yticks([0,100])
    
    if index < 5:
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    else:
        ax.tick_params(bottom="off", top="off", left="off", right="off")
        
    if index == 0:
        ax.text(2005, 10, "Men")
        ax.text(2003, 85, "Women")
    elif index == 5:
        ax.text(2005, 87, "Men")
        ax.text(2003, 7, "Women")
        

# Adds the lib_arts majors plots to the figure object
for index, sp in enumerate(range(1,14,3)):
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[index])
    ax.set_yticks([0,100])
    
    if index < 4:
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    else:
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if index == 0:
        ax.text(2005, 18, "Men")
        ax.text(2003, 78, "Women")

# Adds the other majors plots to the figure object
for index, sp in enumerate(range(2,19,3)):
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[index])
    ax.set_yticks([0,100])
    
    if index < 5:
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    else:
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if index == 0:
        ax.text(2005, 5, "Men")
        ax.text(2003, 90, "Women")
    elif index == 5:
        ax.text(2005, 62, "Men")
        ax.text(2003, 30, "Women")

plt.show()