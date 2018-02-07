from values import sampling_distribution #@UnresolvedImport
import numpy as np

frequencies = []

for stat_test_result, frequency in sampling_distribution.items():
        if stat_test_result >= 2.52:
            frequencies.append(frequency)
            
p_value = np.sum(frequencies) / 1000
print('p_value:', p_value)