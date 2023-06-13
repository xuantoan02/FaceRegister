from fastapi import APIRouter
from api.controler.users import register_user, login_user, protected_route

user = APIRouter()
user.post("/register")(register_user)
user.post("/login")(login_user)
user.get("/protected")(protected_route)
