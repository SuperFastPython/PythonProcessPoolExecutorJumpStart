# SuperFastPython.com
# calculate some large fibonacci numbers sequentially

# calculate the nth fibonacci number
def fibonacci(n):
    # start the sequence
    f0, f1 = 0, 1
    # compute the nth number
    for _ in range(0, n):
        f0, f1 = f1, (f1 + f0)
    return f0

# protect the entry point
if __name__ == '__main__':
    # fibonacci numbers to calculate
    numbers = range(10000)
    # calculate fibonacci numbers
    fibs = map(fibonacci, numbers)
    # store results
    results = dict(zip(numbers, fibs))
    print('Done')