import numpy as np

# This method could be inproved by specifying the order of trying
# different k values. For example, start with average, then continue
# trying average of average and max, recursively loop through these
# averages.

# n th triangle number
def triangular_distance(num) -> int:
    # Optimize efficiency by adding memoization to this function
    # Did not implement because numpy.ndarray is unhashable
    # https://github.com/numpy/numpy/issues/14294
    return np.absolute(num * (num + 1) // 2)

# Naive distance of array value to k
def naive_distance(array, k):
    return np.absolute(array - k)

def solution_1(data)->tuple:
    sum = float('inf')
    pos = -1

    for k in range(data.max() + 1):
        array = naive_distance(data, k)
        temp_sum = np.sum(array)

        if temp_sum < sum:
            sum = temp_sum
            pos = k
    
    return sum, pos

def solution_2(data)->tuple:
    sum = float('inf')
    pos = -1

    for k in range(data.max() + 1):
        array = naive_distance(data, k)
        array = triangular_distance(array)

        temp_sum = np.sum(array)

        if temp_sum < sum:
            sum = temp_sum
            pos = k
    
    return sum, pos

def main():
    data = np.loadtxt('day_7_data.txt', dtype=np.int64, delimiter=',')
    
    # Solution: (fuel, position)
    print(solution_1(data))
    print(solution_2(data))

if __name__ == '__main__':
    main()