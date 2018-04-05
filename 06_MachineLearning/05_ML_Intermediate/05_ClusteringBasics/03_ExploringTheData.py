import pandas as pd

votes = pd.read_csv('114_congress.csv')

senators_per_party = votes['party'].value_counts()
print('Senators Per Party')
print(senators_per_party)

vote_cols = [c for c in votes.columns if not c in ['name', 'party', 'state']]
vote_results = votes[vote_cols].mean()
print('\nVote Results\nNote, > 0.5 means votes passes')
print(vote_results)


# Senators Per Party
# R    54
# D    44
# I     2
# Name: party, dtype: int64
 
# Vote Results
# Note, > 0.5 means votes passes
# 00001    0.325
# 00004    0.575
# 00005    0.535
# 00006    0.945
# 00007    0.545
# 00008    0.415
# 00009    0.545
# 00010    0.985
# 00020    0.525
# 00026    0.545
# 00032    0.410
# 00038    0.480
# 00039    0.510
# 00044    0.460
# 00047    0.370
# dtype: float64