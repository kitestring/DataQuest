#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:41:51 2017

@author: kkite
"""

import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'

def sumdeaths(row):
    dealth_cols = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    death_count = 0
    for col in dealth_cols:
        death = row[col]
        if pd.isnull(death) or death == "NO":
            continue
        if row[col] == 'YES':
            death_count += 1
    return death_count

def joined_accuracy(row):
    
    if pd.isnull(row['Years since joining']) or pd.isnull(row['Year']):
        return False
    else:
        return row['Years since joining'] == (2015 - row['Year'])
    
avengers = pd.read_csv("avengers.csv", encoding='latin-1')

avengers['Year'].hist()
plt.show()

print("The avengers were created in the 1960's therefore no data prior to that data will be consitered in this investigation.")
true_avengers = avengers[avengers['Year'] >= 1960]

print('\n\n\nThe number of deaths is spread over several columns, "Deathn"...\nConvert that information into a single column "Deaths"')
true_avengers['Deaths'] = true_avengers.apply(sumdeaths, axis=1)

# =============================================================================
# Calculate the number of rows where Years since joining is accurate.
#   Because this challenge was created in 2015, use that as the reference year.
#   We want to know for how many rows Years since joining was correctly calculated as the Year value subtracted from 2015.
#   Assign the integer value describing the number of rows with a correct value for Years since joining to joined_accuracy_count.
# =============================================================================

print('\n\n\nVerify that the Years since joning is equal to 2015 - Year\nAssign the result as a boolean in the column "Valid Yesrs Since Joining"')
true_avengers['Valid Yesrs Since Joining'] = true_avengers.apply(joined_accuracy, axis=1)

joined_accuracy_count  = int()
joined_accuracy_count = true_avengers['Valid Yesrs Since Joining'].value_counts().loc[True]
print(joined_accuracy_count)