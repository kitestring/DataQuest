#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:41:51 2017

@author: kkite
"""

import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

def clean_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis=1)

avengers = pd.read_csv("avengers.csv", encoding='latin-1')

avengers['Year'].hist()
plt.show()

print("The avengers were created in the 1960's therefore no data prior to that data will be consitered in this investigation.")
true_avengers = avengers[avengers['Year'] >= 1960]

print('\n\n\nThe number of deaths is spread over several columns, "Deathn"...\nConvert that information into a single column "Deaths"')
true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis=1)
