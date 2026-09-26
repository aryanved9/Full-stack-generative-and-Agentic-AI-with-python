#  static method in python

# static methods are not depended on the objects of the class we can direclty use class and the utility method.

class ChaiUtils:
    @staticmethod
    def clean_method(text):
        return [item.strip() for item in text.split(",")]
    
raw = "ginger,   masala , lemon , water,     milk"

cleaned = ChaiUtils.clean_method(raw)
print(cleaned)