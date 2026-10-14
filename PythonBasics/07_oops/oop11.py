# Property decorator
# Goal to control the value that how we read the value and how we set or edit the value
class TeaLeaf:
    
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <=5:
            self._age = age
        else:
            raise ValueError('Tea age must be in between 1 to 5')

leaf = TeaLeaf(4)
print(leaf.age)

# throw valueErro
# leaf.age = 6
# print(leaf.age)