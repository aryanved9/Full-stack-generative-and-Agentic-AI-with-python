# A local cafe wants a program that suggests a snack.
# if a customer ask for cookies or samosa, it confirms the order. Otherwise, it says it's not available.

snack = input("Enter your preferred snack: ").lower()
print(f"user asked for : {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Great choice ! we'll serve you {snack}")
else:
    print(f"{snack} not available! we only serve cookies and samosa")