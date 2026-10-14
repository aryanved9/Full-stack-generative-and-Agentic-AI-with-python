# creating custom exceptions or raise your own error

def serve_chai(flavor):
    if flavor not in ["masala", "ginger", "lemon"]:
        raise ValueError("flavor not supported..")
    print(f"brewing {flavor} chai...")

serve_chai("mint")

class outOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise outOfIngredientsError("Missing milk or chai")
    print("chai is ready")
    
make_chai(0, 1)