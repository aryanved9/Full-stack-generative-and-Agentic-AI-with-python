# built-in methods/functions

#  Ref : https://docs.python.org/3/builtins/functions.html

def genrate_bill(chai=0,samosa=0):
    """_summary_
    welcome to function docstring

    Args:
        chai (int, optional): _description_. Defaults to 0.
        samosa (int, optional): _description_. Defaults to 0.
    """
    total = chai * 10 + samosa * 10
    return total, "thank you for visiting"
    
print(f"your bill is:", genrate_bill(2,2))
print(genrate_bill.__doc__)
print(genrate_bill.__name__)