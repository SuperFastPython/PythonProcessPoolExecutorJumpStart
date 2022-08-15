# SuperFastPython.com
# example issuing an async task with multiple arguments
from random import random
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# custom function to be executed in a worker process
def task(number, value):
    # report a message
    print(f'Task received {value}', flush=True)
    # block for a moment to simulate work
    sleep(value)
    # return a new value
    return number + value

# protect the entry point
if __name__ == '__main__':
    # create the process pool
    with ProcessPoolExecutor() as exe:
        # issue an asynchronous task
        future = exe.submit(task, 100, random())
        # get the result once the task completes
        result = future.result()
        # report the result
        print(result)
