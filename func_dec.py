from time import time as t

def reader(file, t: type):
    arr = []
    with open(file, 'r') as f:
        for line in f:
            if t == str:
                arr.append(t(line).replace('\n', ''))
            else:
                arr.append(t(line))
    
    return arr

def timer_dec(func):
    def wrapper():
        start = t()
        func()
        end = t()
        print(end - start)
    return wrapper