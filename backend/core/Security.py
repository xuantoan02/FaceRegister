from passlib.context import CryptContext
from core import config


class HashAlgorithm:
    def __init__(self):
        self.SECURITY_ALGORITHM = config.SECURITY_ALGORITHM
        self.SECRET_KEY = config.SECRET_KEY
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str, hash_size=config.HASH_SIZE):
        return self.pwd_context.hash(password, salt_size=hash_size)

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)
