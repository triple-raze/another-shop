from fastapi.responses import JSONResponse
from jose import jwt, ExpiredSignatureError, JWTError
import time
from dotenv import load_dotenv
import os

load_dotenv()

class JWTService:
    jwt_key = os.getenv('JWT_SECRET_KEY')

    @classmethod
    def create_token(cls, user_email: str, lifetime: int) -> str:
        payload = {
            'sub': user_email,
            'iat': int(time.time()),
            'exp': int(time.time()) + lifetime
        }
        return jwt.encode(payload, cls.jwt_key)
    
    @classmethod
    def decode_token(cls, token: str) -> str | Exception:
        try:
            return jwt.decode(token, cls.jwt_key)
        except Exception as error:
            return error
        

    



