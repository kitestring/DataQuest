# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]

female_savings_lst = []
male_savings_lst = []

for n, gen in enumerate(gender):
    if gen == "male":
        male_savings_lst.append(savings[n])
    elif gen == 'female':
        female_savings_lst.append(savings[n])


# Here's a beter way using list comprehension        
# male_savings_lst = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
# female_savings_lst = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

        
female_savings = sum(female_savings_lst) / len(female_savings_lst)
male_savings = sum(male_savings_lst) / len(male_savings_lst)

print(female_savings)
print(male_savings)