#  you're building a ticket info system for railway app. based on seat type, show its features.

seat_type = input(f"Enter seat type (SL,GN,AC,LU) ").lower()

match seat_type:
    case "sl":
        print("No Ac, Bed available")
    case "gn":
        print("cheapest in price")
    case "ac":
        print("ac and bed ")
    case "lu":
        print("bed and meals available")
    case _:
        print("invalid seats")