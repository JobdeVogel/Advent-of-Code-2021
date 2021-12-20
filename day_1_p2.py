import numpy as np
from func_dec import timer_dec

def find_differences(array):
    # Subtract previous element in array from current element
    m_array = np.array([array, np.roll(array, -1), np.roll(array, -2)])
    
    array = sum(m_array)[:-2]

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