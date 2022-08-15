# SuperFastPython.com
# example of getting the result from a completed task
from time import sleep
from concurrent.futures import ProcessPoolExecutor

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
        # get the result from the task, blocks
        result = future.result()
        # report the result
        print(f'Got Result: {result}')
