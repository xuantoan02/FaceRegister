from typing import Optional

from core.Security import HashAlgorithm
from datetime import datetime, timedelta
from core.config import SECRET_KEY, SECURITY_ALGORITHM
from jose import jwt


class AuthUser:
    def __init__(self):
        self.hash_a = HashAlgorithm()

    def authenticate_user(self, user, hashed_password):

        if not user:
            return False
        if not self.hash_a.verify_password(user.password, hashed_password):
            return False

        return True

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
        return access_token
