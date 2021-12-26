import numpy as np

with open('day_8_data.txt', 'r', ) as f:
    data = f.read().splitlines()
    
    new_data = []
    for line in data:
        new_data.append(line.split(' | ')[1].split(' '))

    data = new_data

data = np.array(data)

mylen = np.vectorize(len)
data = mylen(data)

data = data[(data == 2) | (data == 3) | (data == 4) | (data == 7)]
print(data.size)

