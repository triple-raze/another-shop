from typing import Literal
from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserModel(BaseModel):
    id: int 
    name: str = Field(max_length=50)
    gender: Literal['male', 'female']
    email: EmailStr = Field(max_length=150)
    password: str = Field(max_length=50)        # not hashed
    registration_timestamp: date = date.today()
