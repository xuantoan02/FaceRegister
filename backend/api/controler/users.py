from core import config
from ..models.Users import User, UserManager
from core.Security import HashAlgorithm
from fastapi import HTTPException, Depends, UploadFile, File, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from core.Authentication import AuthUser
from datetime import timedelta
from jose import JWTError, jwt
from project.FaceRegister import FaceRegister
from PIL import Image
import io

authUser = AuthUser()
dbUser = UserManager(config.NAME_TABLE_USER)
faceRegister = FaceRegister()


async def register_user(user: User):
    message = None
    if user:
        user_registered = dbUser.get_user(user.user_name)
        if user_registered:
            message = f"User {user.user_name} already exists"
        else:
            message = dbUser.create_user(user)

    return {"message": message}


async def login_user(user: User):
    user_login = dbUser.get_user(user.user_name)
    if not user_login or not HashAlgorithm().verify_password(user.password, user_login[3]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = authUser.create_access_token(
        data={"name": user.user_name, "id": user_login[0]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    return {"access_token": access_token, "token_type": "bearer"}


async def protected_route(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        payload = jwt.decode(credentials.credentials, config.SECRET_KEY, algorithms=[config.SECURITY_ALGORITHM])
        username = payload.get("name")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": f"Hello, {username}! This is a protected route."}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


async def upload_image(image: UploadFile = File(...), id_user: str = Form(...)):
    contents = await image.read()
    path_img = f"assets/images/{image.filename}"
    with open(path_img, "wb") as f:
        f.write(contents)
    a = faceRegister.face_register(id_user, path_img)
    return a
