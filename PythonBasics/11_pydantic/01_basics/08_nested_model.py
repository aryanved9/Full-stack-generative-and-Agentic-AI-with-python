from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address1 = Address(
    street='abc 12',
    city='Ny',
    postal_code='kl009',
)

user = User(
    id=1,
    name='user1',
    address=address1,
)

user_data = {
    'id':2,
    'name':'user2',
    'address':{
        'street': '21abc',
        'city': 'texas',
        'postal_code':'23lkp'
    }
}

user2 = User(**user_data)
print(user)
print(user2)