import bcrypt

class HashService:

    @classmethod
    def hash(cls, password: str) -> bytes:
        password = password.encode()
        salt = bcrypt.gensalt()

        return bcrypt.hashpw(password, salt)
    
    @classmethod
    def check(cls, password: str, hashed_password: bytes) -> bool:
        password = password.encode()

        return bcrypt.checkpw(password, hashed_password)


