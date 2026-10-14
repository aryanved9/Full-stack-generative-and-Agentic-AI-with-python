# Attribute shadowing 

class chai:
    temp = "Hot"
    strength = "Strong"

cutting = chai()
print(cutting.temp)

cutting.temp = "mild"
cutting.cup = "small"
print("after changing", cutting.temp)
print("added cup size to cutting", cutting.cup)
print("From class", chai.temp)

del cutting.temp
del cutting.cup
print('after del cutting temp', cutting.temp)
# print('after del cutting cup', cutting.cup) throw error chai object has no attribut cup for fallback, because we added in object.

# SO the default fallback value in class is called attribute shadowing
