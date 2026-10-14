import threading
import time

def takeOrders():
    for i in range(1,4):
        print(f'Taking order for #{i}')
        time.sleep(2)
        
def BrewingChai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(4)

#  Create thread
order_thread =threading.Thread(target=takeOrders)
brewing_chai = threading.Thread(target=BrewingChai)

order_thread.start()
brewing_chai.start()

order_thread.join()
brewing_chai.join()

print("all orders taken and brewed")