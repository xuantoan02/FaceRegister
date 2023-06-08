from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

import uvicorn
app = FastAPI()

# Kết nối đến cơ sở dữ liệu MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="Admin",
    password="admin",
    database="Faces"
)

# Tạo mô hình dữ liệu Pydantic cho người dùng
class User(BaseModel):
    user_name: str
    password: str

# Định nghĩa CORS để cho phép yêu cầu từ domain khác
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Thay đổi domain tương ứng với frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Định nghĩa endpoint đăng ký người dùng
@app.post("/register")
def register_user(user: User):
    cursor = db.cursor()
    query = "INSERT INTO Users (user_name, password) VALUES (%s, %s)"
    values = (user.user_name, user.password)
    cursor.execute(query, values)
    db.commit()
    return {"message": "User registered successfully"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
