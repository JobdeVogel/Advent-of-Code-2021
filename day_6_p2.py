import numpy as np

DAYS = 256
data = np.loadtxt('day_6_data.txt', dtype=np.int8, delimiter=',')
rate = 7

# The occurance of each value between 0 and rate
occurances = np.array([data[data==i].size for i in range(rate)])
new_values = np.array([], dtype=np.int64)

# Array with new values to be added each day, without reproduction
for day in range(DAYS):
    new_values = np.append(new_values, occurances[day % rate])

amount = data.size

# Add value to amount, and increase values in future days by value
for day in range(DAYS):
    amount += new_values[day]
    new_values[day + rate + 2:DAYS:rate] += new_values[day]

print(amount)