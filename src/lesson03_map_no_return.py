# SuperFastPython.com
# example of executing tasks concurrently with no return
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

# protect the entry point
if __name__ == '__main__':
    # create the process pool
    with ProcessPoolExecutor(4) as exe:
        # issue tasks to execute concurrently
        _ = exe.map(task, range(10))
    # wait automatically for all tasks to finish...
