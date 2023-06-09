from core import config
from ..models.Users import User, UserManager

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
