# what and why?

# Pydantic is a Python library that acts like a strict bouncer for your data, making sure it matches the exact rules and types you expect before your program uses it.

# in short whole job of pydantic is to have the data validation as well as setting management

# with data validation It can also do data parsing can be used for API development, config management, data serilization/deserilization 

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str
    is_active : bool

input_data = {'id': 1, 'name': "Ved", "is_active": True}

user = User(**input_data)
print(user)