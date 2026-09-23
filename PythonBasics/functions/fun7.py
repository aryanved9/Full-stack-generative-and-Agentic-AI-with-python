# args and keyargs

def special_chai(*args, **kargs):
    print("Args", args)
    print("Kargs", kargs)
    
special_chai("cinnamon", "cardmom", sweet = "sugar", liquid = "milk" )

def another_chai(order = None):
    if order is None:
        order = []
    print(order)
    
another_chai()
another_chai(["masala"])