from values import mean_differences #@UnresolvedImport

sampling_distribution = {}

for v in mean_differences:
    
    if sampling_distribution.get(v, False) == False:
        sampling_distribution[v] = 1
    else:
        sampling_distribution[v] += 1
        
print(sampling_distribution)