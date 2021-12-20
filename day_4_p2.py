import numpy as np

# Load board data and numbers
data = np.loadtxt('day_4_data1.txt', dtype=np.int8).reshape((100, 5,5))
numbers = np.loadtxt('day_4_data2.txt', dtype=np.int8, delimiter=',')

# Iterate over numbers
for num in numbers:
    # Replace selected numbers with value -1 on boards
    data = np.where(data != num, data, -1)

    winner_rows = np.where(np.sum(data,axis=2) == -5)
    winner_columns = np.where(np.sum(data,axis=1) == -5)

    # Winner indices of arrays that finished
    winners = np.concatenate([winner_rows[0], winner_columns[0]])

    # If there is a winner, delete it from the board data
    if winners.size > 0:
        # If only one board left, set it to the winner
        if data.shape == (1, 5, 5):
            winner = data[winners]
            
            final_num = num
            break

        data = np.delete(data, winners, axis = 0)

unmarked = winner[winner > -1].sum()
score = unmarked * final_num

print(score)