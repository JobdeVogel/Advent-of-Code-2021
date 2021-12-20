'''
gamma_rate: most common in columns
epshilon_rate: least common in rows
'''

import numpy as np

with open('day_3_data.txt', 'r') as f:
    data = []
    for ins in f:
        bytes = []
        for bit in ins:
            if bit != '\n':
                bytes.append(int(bit))
        data.append(bytes)

np_data = np.array(data, dtype=np.int8)
np_data = np_data.T

most = []
least = []
for array in np_data:
    print(array.shape)
    most.append(np.bincount(array).argmax())
    least.append(np.bincount(array).argmin())


print(most)
print(least)
most = int("".join(map(str, most)))
least = int("".join(map(str, least)))

print(most)
print(least)

res = int(str(most), 2) * int(str(least), 2)

print(int(str(most), 2))
print(int(str(least), 2))
print(res)