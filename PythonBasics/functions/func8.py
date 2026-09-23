# Handle multiple return in python

def chai_stall():
    return 100, 20 ,10

chai_total, sold, remaining = chai_stall()
print("chai total", chai_total)
print("chai sold", sold)
print("remaining", remaining)