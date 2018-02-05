import pandas as pd

flags = pd.read_csv('flags.csv')

reds = flags['red'].tolist()

one_red = sum(reds) / len(reds)
reds.remove(1)

two_red = sum(reds) / len(reds)
reds.remove(1)

three_red = (sum(reds) / len(reds)) * two_red * one_red

print(three_red)