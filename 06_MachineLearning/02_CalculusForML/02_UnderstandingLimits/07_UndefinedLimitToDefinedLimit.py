# See page 3 from math refresher notebook for hand done math steps
# There we use direct substitution to arrive at the answer of -3

import sympy as s

x2,y = s.symbols('x2 y')

y = -x2

limit_four = s.limit(y, x2, 3)
print('limit_four:', limit_four)