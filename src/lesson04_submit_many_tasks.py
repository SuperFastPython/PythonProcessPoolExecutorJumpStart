# SuperFastPython.com
# example issuing many asynchronous tasks systematically
from random import random
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# custom function to be executed in a worker process
def task(number):
    # generate a random value between 0 and 1
    value = random()
    # report a message
    print(f'Task generated {value}', flush=True)
    # block for a moment to simulate work
    sleep(value)
    # return a new value
    return number + value

# protect the entry point
if __name__ == '__main__':
    # create the process pool
    with ProcessPoolExecutor() as ex:
        # issue many asynchronous tasks systematically
        futures = [ex.submit(task, i) for i in range(5)]
        # enumerate futures and report results
        for future in futures:
            print(future.result())
