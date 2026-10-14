# Note: Each object is its own entity, it can posses its own features, its own properties but doesn't bother other ones that's called namespace.

class chai:
    origin = "India"
    
print(chai.origin)
# new property added to class chai
chai.is_hot = True

print(chai.is_hot)

masala_chai = chai()
print("Masala Chai Obj ",masala_chai.origin)
print("Masala Chai Obj ",masala_chai.is_hot)

masala_chai.is_hot = False
# Namspace proved each object has its own entity an by default it doesnt affect others.
print(f"Class value : {chai.is_hot}")
print(f"Masala chai Obj value : {masala_chai.is_hot}")

# can add more properties to object but will not present in class
masala_chai.flavor = "masala"
print("Masala chai flavor prop: ",masala_chai.flavor)
