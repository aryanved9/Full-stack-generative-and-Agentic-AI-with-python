# preparing an order summary with customers names and their total bills
# task: use two list for names and one for bills. print name paid amount

names = ["mohan", "shoan","rohan","jiva"]
bills = [40, 50, 78, 100]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")