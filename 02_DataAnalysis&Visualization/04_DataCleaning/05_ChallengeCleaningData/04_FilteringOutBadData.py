#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:41:51 2017

@author: kkite
"""

import pandas as pd
import matplotlib.pyplot as plt

avengers = pd.read_csv("avengers.csv", encoding='latin-1')

avengers['Year'].hist()
plt.show()

print("The avengers were created in the 1960's therefore no data prior to that data will be consitered in this investigation.")
true_avengers = avengers[avengers['Year'] >= 1960]

