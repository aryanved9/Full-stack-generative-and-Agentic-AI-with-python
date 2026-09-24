from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="No"):
    print(f"serving {type} chai with milk status {milk}")
    
brew_chai("Masala")