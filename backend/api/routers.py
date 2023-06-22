from fastapi import APIRouter
from api.controler.users import *

user = APIRouter()
user.post("/register")(register_user)
user.post("/login")(login_user)
user.get("/protected")(protected_route)
user.post("/upload-avatar")(upload_image)
