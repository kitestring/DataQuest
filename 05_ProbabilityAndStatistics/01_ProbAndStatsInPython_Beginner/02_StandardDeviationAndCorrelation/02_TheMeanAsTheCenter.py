from numpy import median, mean

# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = mean(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  If you'd like, try changing the values around to verify that it still equals 0.
print(sum(differences))


# We can use the median function from numpy to find the median.
# The median is the "middle" value in a set of values. If we sort the values in order, it's the one in the center (or the average of the two in the center if there are an even number of items in the set).
# You'll see that the differences from the median don't always add up to 0.  You might want to play around with this and think about why that is.

values_median = median(values)
median_difference_sum = [v - values_median for v in values]
print(sum(median_difference_sum))