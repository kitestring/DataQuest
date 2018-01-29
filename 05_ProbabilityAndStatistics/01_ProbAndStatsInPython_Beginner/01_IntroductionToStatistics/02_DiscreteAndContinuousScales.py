import matplotlib.pyplot as plt

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

x_data = day_numbers
y_data = [snail_crawl_length, cars_in_parking_lot]
labels = ['snail_crawl_length', 'cars_in_parking_lot']

color_codes = ['red', 'blue', 'green', 'orange', 'black']

fig = plt.figure(figsize=(10, 6)) 

for plot in range(0,2):
    
    plt.plot(x_data, y_data[plot], color=color_codes[plot], label=labels[plot])
  

plt.legend(loc='upper left')
plt.xlabel('day_numbers')
plt.ylabel('Unrelated Shit')
plt.title('This is a completely meaningless plot')    
plt.show()