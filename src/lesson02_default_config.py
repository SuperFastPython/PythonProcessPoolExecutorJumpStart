# SuperFastPython.com
# example reporting the details of a default pool
from concurrent.futures import ProcessPoolExecutor

# protect the entry point
if __name__ == '__main__':
    # create a process pool
    exe = ProcessPoolExecutor()
    # report the status of the process pool
    print(exe._max_workers)
    # shutdown the process pool
    exe.shutdown()
