from core import config
from ..models.Users import User, UserManager

dbUser = UserManager(config.HOST, config.DATABASE, config.ADMIN, config.PASSWORD, config.NAME_TABLE_USER)


async def register_user(user: User):
    message = dbUser.create_user(user)
    if message is not None:
        return {"message": "User registered successfully"}
