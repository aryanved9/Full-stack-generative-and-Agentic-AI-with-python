import threading
import time

def moniter_temp():
    while True:
        print(f"Monitoring tea temp")
        time.sleep()

t = threading.Thread(target=moniter_temp, daemon=True)
t.start()

print("Main program done")

# remove daemon=true then moniter temp will keep excuted even though main thread stopped and all done.