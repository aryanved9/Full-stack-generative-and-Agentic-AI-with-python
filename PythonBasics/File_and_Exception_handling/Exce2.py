# Multiple exceptions

def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        if type(quantity) == int:
            cost = price * quantity
        print(f"total cost : {cost}")
    except KeyError:
        print("Sorry passed item not available")
    except TypeError:
        print("Quantity must be a number")

process_order("ginger",2)
process_order("masala", "two")
process_order("masala", 2)
        