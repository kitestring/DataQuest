# See page 8 from math refresher notebook for hand done math steps

import sympy

rel_min = []
rel_max = []
    
X,y = sympy.symbols('X y')
extreme_one = 0
extreme_two = 2/3

print('extreme_one:', extreme_one)
X = extreme_one - 0.001
start_slope = 3*X**2 - 2*X
print('start_slope:', start_slope)
X = extreme_one + 0.001
end_slope = 3*X**2 - 2*X
print('end_slope:', end_slope)
rel_max.append(extreme_one)


print('\nextreme_two:', extreme_two)
X = extreme_two - 0.001
start_slope = 3*X**2 - 2*X
print('start_slope:', start_slope)
X = extreme_two + 0.001
end_slope = 3*X**2 - 2*X
print('end_slope:', end_slope)
rel_min.append(extreme_two)
 
     
print('\n\nResults')
print('rel_max:', rel_max)
print('rel_min:', rel_min)