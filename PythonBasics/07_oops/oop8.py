# Method Resolution order (MRO), in easy words order of inheritance how it works?

class A:
    label = "A: Cup Tea"

class B(A):
    label = "B: Cup Tea"

class C(A):
    label = "C: Cup Tea"

class D(C,B):
    pass

cupLabel = D()
print(cupLabel.label)

#  output will be C: Cup Tea because the order in which classes passed in inheritance matter. if first have the method it will come from there if not then it will look from second class which is passed.