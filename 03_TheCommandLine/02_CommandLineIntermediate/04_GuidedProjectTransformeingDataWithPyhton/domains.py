import read
import pandas as pd


# read csv file
new_cols = ['submission_time', 'upvotes', 'url', 'headline']
hn_stories = read.load_data('hn_stories.csv', new_cols)

# count the number of occurrences of each domain
top100domains = hn_stories['url'].value_counts()[0:100]
print(top100domains)