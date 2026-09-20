users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 1800, "coupon": "P30"},
    {"id": 1, "total": 900, "coupon": "P40"},
]

discounts = {
    "P20": (0.2, 0),
    "P30": (0.3, 0),
    "P40": (0,20)
}

for user in users:
    percent, flat = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + flat
    print(f"{user["id"]} paid {user['total']} and got discount for next visit of rupees {discount}")