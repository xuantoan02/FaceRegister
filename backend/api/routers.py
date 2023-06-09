from fastapi import APIRouter
from controler.users import register_user

user = APIRouter()
user.post("/register")(register_user)
