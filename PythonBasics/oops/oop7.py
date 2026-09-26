# 3 ways of Access base class, most genral used is Super method.

class Chai:
    
    def __init__(self, type_ , strength):
        self.type = type_
        self.strength = strength
        
# 1st way code duplication

# class GingerChai(Chai):
    
#     def __init__(self, type_, strength, spice_level):  
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# 2nd way  Explicit call, calling base class constructor

# class GingerChai(Chai):
    
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self,type_,strength)
#         self.spice_level = spice_level

# 3rd way

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
        
shop = GingerChai("ginger","strong","medium")
print(f"Our Shop have {shop.type} chai which is {shop.strength} and level of spice is {shop.spice_level}")
        