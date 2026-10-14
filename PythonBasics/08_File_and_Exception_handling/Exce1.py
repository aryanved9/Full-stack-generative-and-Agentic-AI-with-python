# Try except

chai_menu = {"masala": 30, "ginger": 40 }
# chai_menu["elaichi"] error in TERM :  KeyError: 'elaichi'

try:
    chai_menu["elaichi"]
except KeyError:
   print("Key doesn't exists")
   
def serve_chai(flavor):
    try:
        print(f"preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("we don't know the flavor")
    except ValueError as e :
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next order Please !")

serve_chai("Masala")
serve_chai("unknown")
