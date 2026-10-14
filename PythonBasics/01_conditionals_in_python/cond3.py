# A tea stall offer different prices for different cup sizes.
# write a program that calculates the price based on size.

cupSize = input("Enter tea cup size you want (small/medium/large)").lower()

if cupSize == "small":
    print("total price 10")
elif cupSize == "medium":
    print("total price 15")
elif cupSize == "large":
    print("total price 20")
else: print("invalid size input")

