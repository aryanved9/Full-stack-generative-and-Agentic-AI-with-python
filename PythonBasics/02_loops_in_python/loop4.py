#  you're creating a tea menu board. Each item must be numbered.
# task: use enumerate() to print menu items with numbers.

menu = ["green tea", "lemon tea", "masala tea", "mint tea"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item}")