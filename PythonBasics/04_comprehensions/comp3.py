# set comprehension
# {expression for item in iterable if condition}

# in list
fav_chai = ["ginger","lemon","mint","ginger","lemon","masala"]

unique_chai = {chai for chai in fav_chai}
bigger_chai = {chai for chai in fav_chai if len(chai) > 5}

print(f"unique {unique_chai}")
print(f"Bigger {bigger_chai}")

# in dictionary

recipes = {
    "masala chai": ["ginger","cardamom", "clove"],
    "lemon chai": ["lemon","leaf", "clove"],
    "spicy chai": ["ginger","black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(f"Unique spice {unique_spices}")