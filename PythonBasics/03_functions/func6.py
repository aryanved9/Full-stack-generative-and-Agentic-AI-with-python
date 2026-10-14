# Non-local vs Global scopes

# nonlocal
def update_order():
    chai_type = "ginger"
    def kitchen():
        nonlocal chai_type
        chai_type = "Lemon"
    kitchen()
    print(f"update chai type: {chai_type}")
    
update_order()

# global
chai_type = "Irani"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "plain chai"
    kitchen()

front_desk()
print(f"final global chai: {chai_type}")