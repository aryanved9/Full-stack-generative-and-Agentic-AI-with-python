# function scopes : Local, Enclosing from outer function if nested, global top level, built in.

def serve_chai():
    chai_type = 'Masala'  
    # local scope
    print(f"Inside function {chai_type}")
    
chai_type = "Lemon"
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order= "lemon"
    # Enclosing scope
    def print_order():
        chai_order = "ginger"
        print(f"Inner: {chai_order}")
    print_order()
    print(f"Outer: {chai_order}")

chai_order = "mint"
chai_counter()
print(f"global: {chai_order}")