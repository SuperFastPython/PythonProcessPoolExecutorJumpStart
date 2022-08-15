# SuperFastPython.com
# calculate fibonacci numbers using iteration

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
    # calculate some fibonacci numbers
    for i in range(30):
        print(f'f({i}) = {fibonacci(i)}')
