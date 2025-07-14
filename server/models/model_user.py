from typing import Literal
from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import datetime
import re

class UserLogin(BaseModel):
    email: EmailStr = Field(max_length=150)
    password: str = Field(max_length=50)    # not hashed

    @field_validator('password')
    def validate_password(cls, password):
        
        if len(password) < 8:
            raise ValueError('Password length must be at least 8 characters')
        
        if re.search(r'[^a-zA-Z0-9!@#$%^&*_]', password):
            raise ValueError('Only latin letters and "! @ $ % ^ & * _" symbols are allowed')
        
        return password
        

class UserRegistration(UserLogin):
    name: str = Field(max_length=50)
    gender: Literal['male', 'female']


class UserModel(UserRegistration):
    id: int
    created_at: datetime