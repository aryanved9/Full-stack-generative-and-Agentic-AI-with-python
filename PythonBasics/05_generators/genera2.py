# infinite generators

def infinite_chai():
    count = 1
    while True:
        yield f"Refile count #{count}"
        count += 1
        
refill_chai = infinite_chai()
user_refill = infinite_chai()

for _ in range(3):
    print(next(refill_chai))
    
for _ in range(1,6):
    print(next(user_refill))