from functools import reduce
from operator import mul

single_event_probability = 0.5

ten_heads_probability_list = [single_event_probability for _ in range(10)]
print(ten_heads_probability_list)
ten_heads = reduce(mul, ten_heads_probability_list, 1)
print('ten_heads:', ten_heads)

print()

hundred_heads_probability_list = [single_event_probability for _ in range(100)]
print(len(hundred_heads_probability_list))
hundred_heads = reduce(mul, hundred_heads_probability_list, 1)
print('hundred_heads:', hundred_heads)