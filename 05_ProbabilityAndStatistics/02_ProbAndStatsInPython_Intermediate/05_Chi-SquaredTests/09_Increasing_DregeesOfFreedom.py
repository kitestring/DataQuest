Observed_White = 27816
Observed_Black = 3124
Observed_Asian_Pac_Islander = 1039
Observed_Amer_Indian_Eskimo = 311
Observed_Other = 271
total = 32561

Expected_White = 26146.5
Expected_Black = 3939.9
Expected_Asian_Pac_Islander = 944.3
Expected_Amer_Indian_Eskimo = 260.5
Expected_Other = 1269.8

demographics = {'white': [Observed_White, Expected_White],
                'black': [Observed_Black, Expected_Black],
                'Asian_Pac_Islander': [Observed_Asian_Pac_Islander, Expected_Asian_Pac_Islander],
                'Amer_Indian_Eskimo': [Observed_Amer_Indian_Eskimo, Expected_Amer_Indian_Eskimo],
                'Other': [Observed_Other, Expected_Other]}

diffs = []

for group, vals in demographics.items():
    diffs.append((vals[0] - vals[1]) ** 2 / vals[1])
    
race_chisq = sum(diffs)

print(race_chisq)