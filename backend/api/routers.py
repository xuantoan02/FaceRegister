from fastapi import APIRouter
from api.controler.users import register_user

user = APIRouter()
user.post("/register")(register_user)
