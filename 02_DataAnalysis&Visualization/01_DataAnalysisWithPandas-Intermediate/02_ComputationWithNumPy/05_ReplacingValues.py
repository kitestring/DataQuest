import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=1, dtype='U75'))

is_1986 = world_alcohol[:,0] == '1986'
world_alcohol[is_1986,0] = '2014'

is_wine = world_alcohol[:,3] == 'Wine'
world_alcohol[is_wine,3] ='Grog'

print(world_alcohol)