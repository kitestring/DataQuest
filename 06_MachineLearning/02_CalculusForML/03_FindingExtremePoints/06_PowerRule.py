# See page 6 from math refresher notebook for hand done math steps

import sympy as s

x1,x2,y1,y2 = s.symbols('x1 x2 y1 y2')

x1 = 2
x2 = 0

y1 = 5*x1**4
y2 = 9*x2**8

slope_one = y1
slope_two = y2

print('slope_one:', slope_one)
print('slope_two:', slope_two)