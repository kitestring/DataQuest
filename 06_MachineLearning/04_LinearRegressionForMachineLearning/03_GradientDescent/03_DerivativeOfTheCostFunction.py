# page 36 & 37 in the hand written notes for context
# also review the MachineLearning.doc

import pandas as pd

def derivative(a1, xi_list, yi_list):
    
    der = []
    n = len(xi_list)
    for i in range(n):
        der.append(xi_list[i] * ((a1 * xi_list[i]) - yi_list[i]))
    
    return (2/n) * sum(der)

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial):
    a1_list = [a1_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        deriv = derivative(a1, xi_list, yi_list)
        a1_new = a1 - alpha*deriv
        a1_list.append(a1_new)
    return(a1_list)

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

param_iterations = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150)
final_param = param_iterations[-1]
print('final_param:', final_param)

# final_param: 120.142191472