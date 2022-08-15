# SuperFastPython.com
# example running a function in the process pool
from concurrent.futures import ProcessPoolExecutor

# custom function to be executed in a worker process
def task():
    # report a message
    print('This is another process', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the process pool
    with ProcessPoolExecutor() as exe:
        # issue the task
        future = exe.submit(task)
        # wait for the task to finish
        future.result()
    # close the process pool automatically
