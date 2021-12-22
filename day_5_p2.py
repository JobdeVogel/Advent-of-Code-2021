import numpy as np

# Trick to convert data to useful numpy ndarray
with open('day_5_data.txt') as f:
    data = np.loadtxt((x.replace(',',' -> ') for x in f), delimiter=' -> ', dtype=np.int16)
    
    amount_of_values = data.shape[0]
    
    data = data.reshape(amount_of_values, 2, 2)

# Points split in two arrays
value_1 = data[:, 0]
value_2 = data[:, 1]

# Extract all lines that are horizontal, vertical or diagonal
is_hor = value_1[:, 0] == value_2[:, 0]
is_ver = value_1[:, 1] == value_2[:, 1]
is_diag = np.absolute(value_1[:, 0] - value_2[:, 0]) == np.absolute(value_1[:, 1] - value_2[:, 1])

data = data[is_hor | is_ver | is_diag]

# x and y values in points
x_values = data[:, :, 0]
y_values = data[:, :, 1]

# Create drawing board
board = np.zeros([x_values.max() + 1, y_values.max() + 1], dtype=np.int16)

# For each line, add +1 to board at interpolation points between endpoints
for i, (x_value, y_value) in enumerate(zip(x_values, y_values)):
    
    # If this line is diagonal:
    if is_diag[i]:
        x_diff = x_value[1] - x_value[0]
        y_diff = y_value[1] - y_value[0]

        x_dir = np.int8(x_diff / abs(x_diff))
        y_dir = np.int8(y_diff / abs(y_diff))        

        # board[#] where # the range of x1 to x2 and y1 to y2
        board[np.arange(y_value[0], y_value[1] + y_dir, y_dir), np.arange(x_value[0], x_value[1] + x_dir, x_dir)] += 1
    # Else the line is horizontal or vertical:
    else:
        x1 = x_value.min()
        x2 = x_value.max()
        y1 = y_value.min()
        y2 = y_value.max()

        board[y1:y2 + 1, x1:x2 + 1] += 1

# Calculate amount of values above 1
result = board[board > 1].size

print(board)
print(result)