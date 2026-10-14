class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Given chai is not available")
        if not isinstance(cups , int):
            raise TypeError("Number of cups must be an Integer")
        total = menu[flavor] * cups
        print(f"your bill for chai {total}")
    except Exception as e :
        print("Error",e)
    finally:
        print("thank you for visiting")

bill("mint", 2)
bill("masala", "two")
bill("masala", 4)
        