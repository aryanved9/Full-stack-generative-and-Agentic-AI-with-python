# send values to Generators

def chai_order():
    print("welcome ! what chai would you like")
    order = yield
    while True:
        print(f"preparing: {order}")
        order = yield

stall = chai_order()

next(stall)

stall.send("masala chai")
stall.send("lemon chai")