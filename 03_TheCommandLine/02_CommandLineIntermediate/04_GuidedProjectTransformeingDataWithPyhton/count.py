import read
import pandas as pd
from collections import Counter

def df_col_to_string(df):
    combined_string = ''
    for index, row in df.iterrows():
        combined_string += str(row['headline']) + " "
    return combined_string

def remove_insignificant_words(words_lst):
    insignificant_words = ['the','to','a','of','for','in','and','','is','on','with','how','-','your','you','from','why','what','an','are','by','at','show','it']
    return [word for word in words_lst if word not in insignificant_words]
    
# read csv file
new_cols = ['submission_time', 'upvotes', 'url', 'headline']

hn_stories = read.load_data('hn_stories.csv', new_cols)

# combine all the headlines into a single string then split into a list
headlines_str = df_col_to_string(hn_stories)
headlines = headlines_str.lower().split(" ")

# remove insignificant words then count the most common element "word" in the list
headlines = remove_insignificant_words(headlines)
ctr = Counter(headlines)
mostcommonwords = ctr.most_common(100)
print(mostcommonwords)