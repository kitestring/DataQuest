# Compute the mean of car_speeds, and assign the result to mean_car_speed.
# Compute the mean of earthquake_intensities, and assign the result to mean_earthquake_intensities. 
#     Note that this value will not be meaningful, because we shouldn't average values on a logarithmic scale this way.

car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]

mean_car_speed = sum(car_speeds) / len(car_speeds)
print('Mean Car Speed:', mean_car_speed)
mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)
print('Mean Earthquake Intensities:', mean_earthquake_intensities)
print("Note that this value i meaningful, because we shouldn't average values on a logarithmic scale this way.")