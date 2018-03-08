# See page 8 from math refresher notebook for hand done math steps

import sympy

rel_min = []
rel_max = []
    
x,y = sympy.symbols('x y')
extreme_one = 0
extreme_two = 2/3

print('extreme_one:', extreme_one)
x = extreme_one - 0.001
start_slope = 3*x**2 - 2*x
print('start_slope:', start_slope)
x = extreme_one + 0.001
end_slope = 3*x**2 - 2*x
print('end_slope:', end_slope)
rel_max.append(extreme_one)


print('\nextreme_two:', extreme_two)
x = extreme_two - 0.001
start_slope = 3*x**2 - 2*x
print('start_slope:', start_slope)
x = extreme_two + 0.001
end_slope = 3*x**2 - 2*x
print('end_slope:', end_slope)
rel_min.append(extreme_two)
 
     
print('\n\nResults')
print('rel_max:', rel_max)
print('rel_min:', rel_min)