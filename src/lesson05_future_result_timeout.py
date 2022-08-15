# SuperFastPython.com
# example of timeout while waiting for task result
from time import sleep
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import TimeoutError

# task function executed in a worker process
def work():
    # block for a moment
    sleep(1)
    # return a message
    return 'All Done'

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    with ProcessPoolExecutor() as exe:
        # start one task
        future = exe.submit(work)
        try:
            # get the result from the task, blocks
            result = future.result(timeout=0.5)
            # report the result
            print(f'Got Result: {result}')
        except TimeoutError:
            print('Gave up waiting for a result')
