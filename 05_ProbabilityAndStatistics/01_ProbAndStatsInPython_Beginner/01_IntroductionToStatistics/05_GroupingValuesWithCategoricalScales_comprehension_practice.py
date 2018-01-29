# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]

female_savings_lst = [savings[i] for i in range(len(savings)) if gender[i] == 'female']
male_savings_lst = [savings[i] for i in range(len(savings)) if gender[i] == 'male']

        
female_savings = sum(female_savings_lst) / len(female_savings_lst)
male_savings = sum(male_savings_lst) / len(male_savings_lst)

print(female_savings)
print(male_savings)