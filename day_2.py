import numpy as np
from func_dec import reader

horizontal = 0
depth = 0

data = reader('day_2_data.txt', str)

np_data = np.array(data, dtype=str)

for instruction in np_data:
    if 'forward' in instruction:
        horizontal += int(instruction[-1])
    elif 'down' in instruction:
        depth += int(instruction[-1])
    else:
        depth -= int(instruction[-1])

result = horizontal * depth
print(result)

