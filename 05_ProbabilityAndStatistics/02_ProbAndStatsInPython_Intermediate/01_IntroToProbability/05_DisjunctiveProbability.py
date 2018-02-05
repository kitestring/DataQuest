num_list = [i + 1 for i in range(18000)]

hundred_prob_list = [i for i in num_list if i % 100 == 0]
hundred_prob = len(hundred_prob_list) / len(num_list)
print(hundred_prob)

seventy_prob_list = [i for i in num_list if i % 70 == 0]
seventy_prob = len(seventy_prob_list) / len(num_list)
print(seventy_prob)
