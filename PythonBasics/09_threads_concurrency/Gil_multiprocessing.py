from multiprocessing import Process
import time

def crunch_number():
    print(f"started count process...") 
    count = 0
    for _ in range(10_000_000):
        count += 1
    print(f"end the count process...")

if __name__ =="__main__":
    start = time.time()

    p1=Process(target=crunch_number)
    p2=Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"total time with multiprocessing {end-start:.2f} seconds.")
