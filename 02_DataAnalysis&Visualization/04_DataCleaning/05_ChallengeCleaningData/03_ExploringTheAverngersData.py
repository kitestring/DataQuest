#!/usr/bin/env python3


import pandas as pd

avengers = pd.read_csv("avengers.csv", encoding='latin-1')
print(avengers.head(5))

for col in avengers.columns:
    print(col)