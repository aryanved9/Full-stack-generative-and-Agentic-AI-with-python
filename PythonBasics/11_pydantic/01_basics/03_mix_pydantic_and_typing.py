from pydantic import BaseModel
from typing import List, Optional, Dict

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
   
class Blog(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

cart_data = {
    "user_id": 12,
    "items": ["laptop", "mobile"],
    "quantities": {"laptop": 2 , "mouse":4, "mobile":0}
}

cart_item1 = Cart(**cart_data)
print(cart_item1)