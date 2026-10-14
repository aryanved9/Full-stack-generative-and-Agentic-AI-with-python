# self argument in python

class ChaiCup:
    size = 150
    
    def describe(self):
        return f"{self.size}ml chai cup"

cup = ChaiCup()

print(f"calling from obj chai: {cup.describe()}")
print(f"calling from class: {ChaiCup.describe(cup)}")

cupTwo = ChaiCup()
cupTwo.size = 100

print(f"calling from cupTwo: {cupTwo.describe()}")
print(f"calling from cupTwo using class: {ChaiCup.describe(cupTwo)}")