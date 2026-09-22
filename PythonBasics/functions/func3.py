# introduction to return keyword

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(2,15)
print("Table 1 bill: ",my_bill)
print(f"Table 2 bill: ", calculate_bill(3,15))