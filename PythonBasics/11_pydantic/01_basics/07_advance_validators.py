from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    firstname: str
    lastname: str
    
    @field_validator('firstname','lastname')
    def name_must_capitalize(cls, v):
        if not v.isTitle():
            raise ValueError("Names must capitalized")
        return v

class User(BaseModel):
    email: str
    
    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()

email = User(email='Aryan@gmail.com')
print(email)

class Product(BaseModel):
    price : str
    
    @field_validator('price', mode='before')
    def parse_price(cls,v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v

class DateRange(BaseModel):
    start_date : datetime
    end_date: datetime
    
    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date > values.end_date:
            raise ValueError("End date must be after start date")
        return values
    