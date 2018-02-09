males_proportion = 0.669
females_proportion = 0.331
earn_over_50k = 0.241
earn_under_50k = 0.759
total_population = 32561

# Calculate the expected value for Males who earn >50k, and assign to males_over50k.
males_over50k = total_population * males_proportion * earn_over_50k
print('males_over50k:', males_over50k)

# Calculate the expected value for Males who earn <=50k, and assign to males_under50k.
males_under50k = total_population * males_proportion * earn_under_50k
print('males_under50k:', males_under50k)

# Calculate the expected value for Females who earn >50k, and assign to females_over50k.
females_over50k = total_population * females_proportion * earn_over_50k
print('females_over50k:', females_over50k)

# Calculate the expected value for Females who earn <=50k, and assign to females_under50k.
females_under50k = total_population * females_proportion * earn_under_50k
print('females_under50k:', females_under50k)