from pydantic import BaseModel

class CartProductModel(BaseModel):
    id: int 
    user_id: int
    product_id: int