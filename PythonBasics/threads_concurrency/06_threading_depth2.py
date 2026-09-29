import threading
import time

def prepare_chai(chai_type, wait_time):
    print(f"{chai_type} chai brewing..")
    time.sleep(wait_time)
    print(f"{chai_type} chai ready.")

t1 = threading.Thread(target=prepare_chai, args=("masala",2))
t2 = threading.Thread(target=prepare_chai,args=("Ginger",3))

t1.start()
t2.start()

t1.join()
t2.join()