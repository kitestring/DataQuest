import read
import pandas as pd
from dateutil.parser import parse
from datetime import datetime

# read csv file
new_cols = ['submission_time', 'upvotes', 'url', 'headline']
hn_stories = read.load_data('hn_stories.csv', new_cols)


def parse_time(s, time_format):
    try:
        ret = parse(s)
    except ValueError:
        ret = datetime.utcfromtimestamp(s)
        
    if time_format == 'hour':
        return ret.hour
    elif time_format == 'day':
        return ret.day

# create new column that has the hour of the submission hour
hn_stories['submission_hour'] = hn_stories['submission_time'].apply(parse_time, args=('hour',))

# determine the most common submission hours
hn_stores_submission_hour_frequency = hn_stories['submission_hour'].value_counts()
print(hn_stores_submission_hour_frequency)

# create new column that has the hour of the submission hour
hn_stories['submission_day'] = hn_stories['submission_time'].apply(parse_time, args=('day',))

# determine the most common submission hours
hn_stores_submission_day_frequency = hn_stories['submission_day'].value_counts()
print(hn_stores_submission_day_frequency)