# pages 34 - 36 in the hand written notes for context

def test_homog(x3):
    x1 = 4/3*x3
    x2 = 0
    
    return ((x1 + (5/3)*x2 - (4/3)*x3)==0) and (x2==0)


b_one = test_homog(1)

b_two = test_homog(-10)

print('b_one:', b_one)
print('b_two:', b_two)

# Notice that it doesn't matter which form we use, this is math
# so long as we follow the rules each of these are the same.

def test_homog_2(x3):
    x1 = 4/3*x3
    x2 = 0
    
    return ((3*x1 + 5*x2 - 4*x3==0)) and (3*x2==0)

b_one_sanity_check = test_homog_2(1)

b_two_sanity_check = test_homog_2(-10)

print('b_one_sanity_check:', b_one_sanity_check)
print('b_two_sanity_check:', b_two_sanity_check)