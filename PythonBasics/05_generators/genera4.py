# yield from and close the generator

def local_chai():
    yield "Masala chai"
    yield "ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
for chai in full_menu():
    print(f"final Menu: {chai}")
    
def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed ! No more chai")
        
stall = chai_stall()

print(next(stall))
stall.close() 
# it triggers a generators exit method which actually is responsible for this. so this not only close this, this is actually a cleanup