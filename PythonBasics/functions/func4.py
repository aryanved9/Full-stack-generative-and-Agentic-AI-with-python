# improve Traceability while writing or while defining functions.

#  you shop adds a 10% VAT on every order. you want this to be traceable and consistent.
#  Task: write add_vat(price, vat_rate) and use it to compute final prices for 3 orders.

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [50, 40 ,60]

for price in orders:
    final_price = add_vat(price, 10)
    print(f"original price: {price}, final with VAT: {final_price}")