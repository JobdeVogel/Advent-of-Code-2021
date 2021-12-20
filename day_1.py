import numpy as np
from func_dec import timer_dec

def find_differences(array):
    # Subtract previous element in array from current element
    diff = np.subtract(array, np.roll(array, 1))
    # First value is 0
    diff[0] = 0

    # Print the size of array with positive values
    print(diff[diff > 0].size)

@timer_dec
def main():
    f = 'day_1_data.txt'

    # Load file to numpy array
    array = np.loadtxt(f, dtype=int)
    #with open(f) as f:
    #    array = np.array([line.strip().split() for line in f],float)

    find_differences(array)

main()

@timer_dec
def casual():
    len = 0
    with open('day_1_data.txt', 'r') as f:
        prev = 0
        for i, line in enumerate(f):
            val = int(line)
            if i != 0: 
                if val - prev > 0:
                    len += 1
        
            prev = val

        print(len)

casual()