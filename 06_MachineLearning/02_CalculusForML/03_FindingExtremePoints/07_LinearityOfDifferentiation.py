# See page 7 from math refresher notebook for hand done math steps

import sympy as s

x1,x2,y1,y2 = s.symbols('x1 x2 y1 y2')

x1 = 1
x2 = 2

y1 = 5*x1**4 - 1
y2 = 3*x2**2 - 2*x2

slope_three = y1
slope_four = y2

print('slope_three:', slope_three)
print('slope_four:', slope_four)