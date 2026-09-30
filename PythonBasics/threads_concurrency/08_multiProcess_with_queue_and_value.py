# Inefficient Thread approach.

# import threading
# import time

# def cpu_heavy():
#     print(f"crunching some numbers...")
#     total = 0
#     for i in range(10**7):
#         total += i
#     print("Done")

# start = time.time()
# threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# [t.start() for t in threads]
# [t.join() for t in threads]

# print(f"Time taken : {time.time() - start:.2f} seconds")


# Efficient approach with multiProcess
from multiprocessing import Process
import time

def cpu_heavy():
    print(f"crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print("Done")

if __name__ == '__main__':
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]

    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken : {time.time() - start:.2f} seconds")