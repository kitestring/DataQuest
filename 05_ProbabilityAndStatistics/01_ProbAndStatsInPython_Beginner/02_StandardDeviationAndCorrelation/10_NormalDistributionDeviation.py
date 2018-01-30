from Stats_Functions import std_dev, within_percentage

# Housefly wing lengths in millimeters
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 
                42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 
                45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 
                47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 
                50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]

mean_wing_lengths = sum(wing_lengths) / len(wing_lengths)
std_dev_wing_lengths = std_dev(wing_lengths)

# For each point in wing_lengths, calculate the distance from the mean in number of standard deviations.
SD_count_wing_lengths = [(wl - mean_wing_lengths) / std_dev_wing_lengths for wl in wing_lengths]

# Calculate the proportion of the data that's within one standard deviation of the mean. Assign the result to within_one_percentage.
within_one_percentage = within_percentage(SD_count_wing_lengths, 1)
within_two_percentage = within_percentage(SD_count_wing_lengths, 2)
within_three_percentage = within_percentage(SD_count_wing_lengths, 3)

print('within_one_percentage:', within_one_percentage)
print('within_two_percentage:', within_two_percentage)
print('within_three_percentage:', within_three_percentage)