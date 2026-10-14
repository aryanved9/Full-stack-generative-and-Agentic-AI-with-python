# you run an online tea store. if the order amount is more 300, delivery is free otherwise 30 rupee.
# note Input order_amount , Use ternary operator to decide delivery fee.

order_amount = int(input("Enter the order amount "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"delivery fees is: {delivery_fees}")