# simulate tea heating its starts at 40c and boils at 100c 
# task : Use while loop, increase temp by 15 until reaches or exceed 100, print each temp steps.

initialTemp = 40

while initialTemp <= 100:
    print(f"current temp {initialTemp}")
    initialTemp = initialTemp + 15

print("Tea is boiled")