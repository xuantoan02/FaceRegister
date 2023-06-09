# from fastapi import FastAPI
# from api import routers
# from fastapi.middleware.cors import CORSMiddleware
#
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Thay đổi domain tương ứng với frontend
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# app.include_router(routers.user)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    email: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def get_user(user_name):
    return user_name


def user_exists(username):
    return False


def save_user(username,a,b):
    return True


def get_password_hash(password: str):
    return pwd_context.hash(password, salt_size=32)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    # Kiểm tra xem người dùng có tồn tại không
    user = get_user(username)
    if not user:
        return False

    # Kiểm tra mật khẩu
    if not verify_password(password, user["password"]):
        return False

    return True


@app.post("/register")
async def register(user: User):
    # Kiểm tra xem người dùng đã tồn tại chưa
    if user_exists(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")

    # Mã hóa mật khẩu
    hashed_password = get_password_hash(user.password)

    # Lưu thông tin người dùng vào cơ sở dữ liệu (hoặc nơi lưu trữ khác)
    save_user(user.username, hashed_password, user.email)

    # Trả về thông báo thành công
    return {"message": "User registered successfully"}


@app.post("/token")
async def login(username: str, password: str):
    # Xác thực người dùng
    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Tạo mã thông báo (JWT)
    access_token = create_access_token(username)

    # Trả về mã thông báo
    return {"access_token": access_token, "token_type": "bearer"}
def create_access_token(username: str, expires_delta: timedelta = timedelta(minutes=15)):
    expire = datetime.utcnow() + expires_delta
    payload = {"sub": username, "exp": expire}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token