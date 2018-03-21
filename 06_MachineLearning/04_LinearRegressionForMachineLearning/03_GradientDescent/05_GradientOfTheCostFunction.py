# page 36 & 37 in the hand written notes for context
# also review the MachineLearning.doc

import pandas as pd

def a0_derivative(a0, a1, xi_list, yi_list):
    n = len(xi_list)
    error = 0
    for i in range(n):
        error += a0 + (a1 * xi_list[i]) - yi_list[i]
    return (2/n) * error

def a1_derivative(a0, a1, xi_list, yi_list):
    n = len(xi_list)
    error = 0
    for i in range(n):
        error += xi_list[i] * (a0 + (a1 * xi_list[i]) - yi_list[i])
    return (2/n) * error

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial, a0_initial):
    a1_list = [a1_initial]
    a0_list = [a0_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        a0 = a0_list[i]
        
        a1_deriv = a1_derivative(a0, a1, xi_list, yi_list)
        a0_deriv = a0_derivative(a0, a1, xi_list, yi_list)
        
        a1_new = a1 - alpha*a1_deriv
        a0_new = a0 - alpha*a0_deriv
        
        a1_list.append(a1_new)
        a0_list.append(a0_new)
    return(a0_list, a1_list)

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

a0_params, a1_params = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150, 1000)
print('a0_params:', a0_params)
print('a1_params:', a1_params)

# a0_params: [1000, 999.97297978123288, 999.98590370106604, 999.98023254713905, 999.98321790150521, 999.9821734177915, 999.98300493236297, 999.98296311912168, 999.98332786351068, 999.98350334433997, 999.98376693244177, 999.98398950421347, 999.98423117017433, 999.98446394725659, 999.98470086233294, 999.98493585104279, 999.98517173650964, 999.9854072044933, 999.98564286680801, 999.98587843863777, 999.98611405257202]
# a1_params: [150, 105.34801721547944, 126.13471917628125, 116.45794862200977, 120.96274606972909, 118.86564116059868, 119.84189984026605, 119.38742488614261, 119.59899502291616, 119.50050320781361, 119.54635359313434, 119.52500879150305, 119.53494516153384, 119.53031930255781, 119.53247255390217, 119.53146994657168, 119.53193647656232, 119.53171908350993, 119.53182007507831, 119.53177285001942, 119.53179462379771]
