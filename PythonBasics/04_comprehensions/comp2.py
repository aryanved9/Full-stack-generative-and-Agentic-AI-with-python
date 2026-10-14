# List comprehension
# [expression for item in iterable if condition]

menu = ["Masala chai", "Iced lemon tea", "Green tea", "Ginger tea", "Iced peach tea"]

Iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]
print(Iced_tea)