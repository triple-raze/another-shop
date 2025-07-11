from typing import Literal
from pydantic import BaseModel, Field, field_validator, EmailStr 
from datetime import datetime
import re

class UserForm(BaseModel):
    name: str = Field(max_length=50)
    gender: Literal['male', 'female']
    email: EmailStr = Field(max_length=150)
    password: str = Field(max_length=50)    # not hashed

    @field_validator('password')
    def validate_password(cls, password):

        if len(password) < 8:
            raise ValueError('Password length must be at least 8 characters')
        
        if re.search(r'\W'):    # characters that arent in [a-z] [A-Z] [0-9] _ 
            raise ValueError('Only latin letters and underscores are allowed')
        

class UserEntity(UserForm):
    id: int
    created_at: datetime