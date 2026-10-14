# walrus operator assigns values to variables as part of a large expression, walrus name due to its resemblance to eyes and tusks of walrus.

value = 13

if remainder := value % 5:
    print(f"remainder is {remainder}")
    
available_sizes = ["small", "medium", "large"]

if(requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"serving {requested_size} chai")
else:
    print(f"size is unavailable {requested_size}")
    

flavors = ["masala","ginger","lemon","mint"]

print("Available flavors: ", flavors)

while(flavor := input("Choose your flavor: ")) not in flavors:
    print(f"sorry, {flavor} is not available")

print(f"you choose {flavor} chai")