# SuperFastPython.com
# example of setting a large number number of workers
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# custom task function executed in the process pool
def task(number):
    # block for a moment
    sleep(1)
    # report a message
    if number % 10 == 0:
        print(f'>task {number} done', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    with ProcessPoolExecutor(50) as exe:
        # issue many tasks to the pool
        _ = exe.map(task, range(50))
