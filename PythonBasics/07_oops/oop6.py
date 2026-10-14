#  Inheritance and composition in python classes

class BaseChai:
    def __init__(self, type_):
        self.type = type_
        
    def prepare_chai(self):
        print(f"preparing {self.type} chai..")

class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding cardmom, ginger,cloves ")

class ChaiShop:
    # here holding a class any of it in a variable, on first line we have not used inherting syntax.
    # here actually keeping a refrence of the BaseChai, chai_cls get refrence to everything of BaseChai then you dont put the parenthesis inside the class. that's the syntax of composition. 
    #chai_cls = BaseChai is not itself the composition. It is a class reference used to create the composed object. The actual composition is: self.chai = self.chai_cls("Regular") because the ChaiShop object contains/has a chai object.
    chai_cls = BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")
    
    def serve(self):
        print(f"serving {self.chai.type} chai in the shop")
        self.chai.prepare_chai()
        
class NewChaiShop(ChaiShop):
    chai_cls = MasalaChai
    
shop = ChaiShop()
newchai = NewChaiShop()

shop.serve()
newchai.serve()
newchai.chai.add_spices()