staff = [("sohan", 16), ("rohan", 15), ("tina", 17), ("Tina", 14)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to mange the staff")
        break
else:
    print("no one is eligible to manage the staff")