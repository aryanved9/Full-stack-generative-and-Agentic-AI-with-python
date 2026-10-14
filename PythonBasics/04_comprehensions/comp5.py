# Generator comprehensions for memory optimization
# (expression for item in iterable if condition)
# generator works in stream of values means 1 by 1 . not all at once.

daily_sales = [5,10,12,7,3,8,9,15]
# assume we need sum of all sales above 5.
# memory efficient operation.
 
total = sum(sale for sale in daily_sales if sale > 5 )
print(f"Total: {total}")