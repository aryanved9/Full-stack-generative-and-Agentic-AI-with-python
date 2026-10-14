# one of the most comman term that we see all around the places is yield. this is keyword just like for keyword,
# but generators are always, always going to come up with the yield as a keyword.

# things need to always remember about generators is first of all you save memory, sometimes you don't want results immediately and lazy evaluation.


# regular function
def chai_order():
    return ["cup 1", "cup 2", "cup 3"] 

# Generator function

def serve_chai():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

serve_value = serve_chai()
# serve value getting generator object and holding ref to the function

print(next(serve_value))
# next will run the function once give first yield value and function stops there. when next time next will it start from there. it actually keep tracks everything in memory.
print(next(serve_value))
print(next(serve_value))
