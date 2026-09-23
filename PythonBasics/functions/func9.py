# Types of functions Pure & Impure, Recursive functions, Lambdas functions(Anonymous function.)

def pure_fn(cups):
    return cups * 10

total_chai = 0
#  not recommended
def Impure_fn(cups):
    global total_chai
    total_chai += cups
    
# Recursive

def call_chai(n):
    print(n)
    if n == 0:
        return "all cups called"
    
    return call_chai(n-1)
    
val = call_chai(3)
print(val)

# lambdas

chai_types = ["ginger","kadak","masala","kadak","lemon"]

strong_chai = list(filter(lambda chai_type: chai_type == "kadak" , chai_types))
print(strong_chai)