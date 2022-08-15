# SuperFastPython.com
# example of executing multiple tasks in chunks
from concurrent.futures import ProcessPoolExecutor

# custom function to be executed in a worker process
def task(number):
    return number*2

# protect the entry point
if __name__ == '__main__':
    # create the process pool
    with ProcessPoolExecutor(4) as exe:
        # issue tasks to execute concurrently
        _ = exe.map(task, range(10000), chunksize=500)
    # wait for all tasks to complete
    print('All done')
