from multiprocessing import Process
import time

def brew_chai(chai_type):
    print(f"start of {chai_type} chai brewing")
    time.sleep(3)
    print(f"end of {chai_type} chai brewing")
    
if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"chai maker #{i + 1}",))
        for i in range(3)
    ]
    # start all process
    for p in chai_makers:
        p.start()
    
    # wait for all to complete
    for p in chai_makers:
        p.join()
        
    print("All chai served")