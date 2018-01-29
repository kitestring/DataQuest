# This is the worst mission to date.


# You may be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication or division first; the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction. Otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2. The result is the same (2/2 == 2 * 1/2).
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same is true for subtraction and addition.
# In this case, we need to convert subtraction into adding a negative number. If we don't we'll end up subtracting more than we expect.
b = 10 - 8 + 5
# Add -8 instead of subtracting 8.
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)

c = 10 * 2 + 5
d = 3 - 1 / 2 - 2