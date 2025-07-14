from pydantic import BaseModel

class CartProductModel(BaseModel):
    user_id: int
    product_id: int