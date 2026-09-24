from functools import wraps

# the whole job wrap is to preserve metadata.

def my_decorator(function):
    @wraps(function)
    def wrapper():
        print("Before function runs")
        function()
        print("after function runs")
    return wrapper

@my_decorator
def greet():
    print("hello from decorator! greeting to you")
    
greet()
print(greet.__name__)