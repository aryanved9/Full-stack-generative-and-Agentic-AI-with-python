#  In general serialization is a process of converting complex data str. like pydantic models into something which is much more easily stored, transmitted and can be processed as well.
#  Pydantic mode -> Python Dict, JSON string

from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email : str
    is_active: bool
    createdAt: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders= {datetime: lambda v: v.strftime('%d-%m-%y %H: %M %S')}
    )

user = User(
    id = 1,
    name =  'Nakul',
    email="abc@gmail.com",
    is_active=True,
    createdAt=datetime(2026, 5, 15 , 14 , 55, 23),
    address=Address(
        street = 'abc Street',
        city = 'NY',
        zip_code = '454zip'
    ),
    tags=['subscriber', 'premium']
)

python_dic = user.model_dump()
print(python_dic)
python_json = user.model_dump_json()
