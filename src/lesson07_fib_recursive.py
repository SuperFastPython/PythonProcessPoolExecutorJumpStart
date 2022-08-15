# SuperFastPython.com
# calculate fibonacci numbers using recursion

# calculate the nth fibonacci number
def fibonacci(n):
    # check for the start of the sequence
    if n <= 1:
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

# protect the entry point
if __name__ == '__main__':
    # calculate some fibonacci numbers
    for i in range(30):
        print(f'f({i}) = {fibonacci(i)}')
