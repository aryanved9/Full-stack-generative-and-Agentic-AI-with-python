import threading
import time

def boil_milk():
    print(f"{threading.current_thread().name} boiling milk...")
    time.sleep(2)
    print(f"{threading.current_thread().name} milk boiled.")

def toast_bun():
    print(f"{threading.current_thread().name} toasting bun...")
    time.sleep(3)
    print(f"{threading.current_thread().name} Toast ready.")

start = time.time()

t1 = threading.Thread(target=boil_milk, name="Milk thread")
t2 = threading.Thread(target=toast_bun, name="Toast thread")

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"breakfast ready {end-start:.2f} seconds")