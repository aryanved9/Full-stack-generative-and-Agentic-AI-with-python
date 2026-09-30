from multiprocessing import Process, Value

def increment(counter):
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    Processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in Processes]
    [p.join() for p in Processes]
    
    print(f"Final counter value: ", counter.value)