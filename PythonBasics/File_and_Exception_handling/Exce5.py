# Traditional way file handling
# file = open("order.txt","w")
# try:
#     file.write("ordering masala chai")
# finally:
#     file.close() 

# Modern way with operator
with open("order.txt", "w") as file:
    file.write("ordering ginger tea") 
