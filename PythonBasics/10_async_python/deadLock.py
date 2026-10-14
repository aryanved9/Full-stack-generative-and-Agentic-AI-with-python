import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 lock a accquired")
        with lock_b:
            print("Task 1 lock b accquired")

def task2():
    with lock_b:
        print("Task 2 lock b accquired")
        with lock_a:
            print("Task 2 lock a accquired")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()