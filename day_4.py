import numpy as np

data = np.loadtxt('day_4_data1.txt', dtype=np.int8).reshape((100, 5,5))

numbers = np.loadtxt('day_4_data2.txt', dtype=np.int8, delimiter=',')

for i, num in enumerate(numbers):
    data = np.where(data != num, data, -1)
    
    winner_rows = np.where(np.sum(data,axis=2) == -5)
    winner_columns = np.where(np.sum(data,axis=1) == -5)

    winner = False
    winner_board = ''

    if winner_rows[0].size > 0:
        winner_board = data[winner_rows[0]]
        winner = True
    
    elif winner_columns[0].size > 0:
        winner_board = data[winner_columns[0]]
        winner = True

    if winner:
        print(winner_board)
        unmarked = winner_board[winner_board > -1].sum()

        score = unmarked * num
        print('Final number: ' + str(num))
        print('Winner found in iteration: ' + str(i))
        break

print('Score: ' + str(score))