import numpy as np

# My initial not so smart idea to solve this problem
# Check p2 for optimized solution
DAYS = 80
data = np.loadtxt('day_6_data.txt', dtype=np.int8, delimiter=',')

for _ in range(DAYS):
    zeros = np.where(data == 0)
    not_zeros = np.where(data > 0)

    data[zeros] = 6
    data[not_zeros] -= 1
    
    new_values = np.tile(8, zeros[0].size)
    data = np.append(data, new_values)

print(data.size)