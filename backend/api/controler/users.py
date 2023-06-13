from core import config
from ..models.Users import User, UserManager
from core.Security import HashAlgorithm
from fastapi import HTTPException,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from core.Authentication import AuthUser
from datetime import timedelta
from jose import JWTError, jwt

authUser = AuthUser()
dbUser = UserManager(config.HOST, config.DATABASE, config.ADMIN, config.PASSWORD, config.NAME_TABLE_USER)


async def register_user(user: User):
    message = None
    if user:
        user_registered = dbUser.get_user(user.user_name)
        if user_registered:
            message = "User already exists"
        else:
            message = dbUser.create_user(user)

    return {"message": message}


async def login_user(user: User):
    user_login = dbUser.get_user(user.user_name)
    if not user_login or not HashAlgorithm().verify_password(user.user_name, user_login[2]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = authUser.create_access_token(
        data={"sub": user.user_name},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    return {"access_token": access_token, "token_type": "bearer"}


async def protected_route(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        payload = jwt.decode(credentials.credentials, config.SECRET_KEY, algorithms=[config.SECURITY_ALGORITHM])
        print(credentials.credentials)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": f"Hello, {username}! This is a protected route."}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
