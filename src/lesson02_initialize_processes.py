# SuperFastPython.com
# example initializing worker processes in the pool
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# custom function to be executed in a worker process
def task(number):
    # report a message
    print(f'Worker task {number}...', flush=True)
    # block for a moment
    sleep(1)

# initialize a worker in the process pool
def init():
    # report a message
    print('Initializing worker...', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with ProcessPoolExecutor(2,
        initializer=init) as exe:
        # issue tasks to the process pool
        _ = exe.map(task, range(4))
