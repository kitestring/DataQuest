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

