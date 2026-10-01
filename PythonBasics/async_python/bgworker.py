import asyncio
import threading
import time

def bgWorker():
    while True:
        time.sleep(1)
        print(f"logging the system health...")
        
async def fetch_order():
    await asyncio.sleep(2)
    print(f"order fetched")
    
threading.Thread(target=bgWorker, daemon=True).start()
asyncio.run(fetch_order())  