import numpy as np
from func_dec import reader, timer_dec

horizontal = 0
depth = 0
aim = 0

data = reader('day_2_data.txt', str)

np_data = np.array(data, dtype=np.unicode_)

for instruction in np_data:
    if 'forward' in instruction:
        horizontal += int(instruction[-1])
        depth += aim * int(instruction[-1])
    elif 'down' in instruction:
        aim += int(instruction[-1])
    else:
        aim -= int(instruction[-1])
    print(horizontal)
    print(depth)
    print(aim)
    print('\n')

result = horizontal * depth
print(result)

