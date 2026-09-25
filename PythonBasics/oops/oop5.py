# constructors and init in python

class ChaiOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("masala", 200)
order_two = ChaiOrder("ginger", 220)

print(order.summary())
print(order_two.summary())