import numpy as np

# Trick to convert data to useful numpy ndarray
with open('day_5_data.txt') as f:
    data = np.loadtxt((x.replace(',',' -> ') for x in f), delimiter=' -> ', dtype=np.int16)
    
    amount_of_values = data.shape[0]
    
    data = data.reshape(amount_of_values, 2, 2)

# Points split in two arrays
value_1 = data[:, 0]
value_2 = data[:, 1]

# All line indices where x1 == x2 or y1 == y2
data = data[(value_1[:, 0] == value_2[:, 0]) | (value_1[:, 1] == value_2[:, 1])]

# x and y values in points
x_values = data[:, :, 0]
y_values = data[:, :, 1]

# Create drawing board
board = np.zeros([x_values.max() + 1, y_values.max() + 1], dtype=np.int8)

# For each line, add +1 to board at interpolation points between endpoints
for x_value, y_value in zip(x_values, y_values):
    x1 = x_value.min()
    x2 = x_value.max()
    y1 = y_value.min()
    y2 = y_value.max()

    board[y1:y2 + 1, x1:x2 + 1] += 1

# Calculate amount of values above 1
result = board[board > 1].size
print(result)
