from pydantic import BaseModel, Field

class ProductModel(BaseModel):
    name: str = Field(max_length=50)
    description: str = Field(max_length=1000)
    price: int
    old_price: int | None