# classMethod vs staticMethod, in short classmethod is decorator genrally used for multiple constructor in a class well not exactlly but seems that yes we have muliple constructor

class ChaiOrder:
    
    def __init__(self, chai_type, sweetness, size):
        self.type = chai_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
                order_data["chai_type"],
                order_data["sweetness"],
                order_data["size"]
        )
    @classmethod
    def from_string(cls, order_data):
        chai_type, sweetness, size = order_data.split("-")
        return cls(chai_type,sweetness,size)
    
    @staticmethod
    def is_valid_size(size):
        return size in ["small","medium","large"]
 
print(ChaiOrder.is_valid_size("small"))   
 
order = ChaiOrder.from_dict({"chai_type":"masala", "sweetness":"medium", "size":"large"})
order2 = ChaiOrder.from_string("ginger-low-small")
order3 = ChaiOrder("lemon","low","medium")
print(order.__dict__)
print(order2.__dict__)
print(order3.__dict__)