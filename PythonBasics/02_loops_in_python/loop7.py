# some chai flavours are out of stock. you want to skip those and stop entirely if someone request a restricted flavour.
# task:  skip if flavour out of stock, break if flavour is discontinued.

flavours = ["ginger", "masala", "out of stock", "discontinued","mint"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"current item flavour: {flavour}")

print("outside loop")