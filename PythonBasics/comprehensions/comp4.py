# Dictionary comprehension
# {expression for item in iterable if condition} only diff expression = key: value pair

tea_price_inr = {
    "masala chai": 40,
    "green tea": 50,
    "lemon tea": 200
}

tea_price_usd = { tea: price / 80 for tea, price in tea_price_inr.items() }
print(tea_price_usd)