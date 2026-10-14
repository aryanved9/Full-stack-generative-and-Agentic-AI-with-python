from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=15,
        description="Employee Name",
        examples='Rajat singh'
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )

class User(BaseModel):
    email: str = Field(..., pattern=r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$')
    phone: str = Field(..., pattern=r'^[6-9]\d{9}$')
    age: int = Field(
        ...,
        ge=0,
        le=100,
        description="age in years",
    )
    discount: float = Field(
        ...,
        ge = 0,
        le= 100,
        description='discount percentage'
    )