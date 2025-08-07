from pydantic import BaseModel

class JWTModel(BaseModel):
    refresh_token: str