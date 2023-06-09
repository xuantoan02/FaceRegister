from core.Security import HashAlgorithm


class AuthUser:
    def __init__(self):
        self.hash_a = HashAlgorithm()

    def authenticate_user(self, user, hashed_password):

        if not user:
            return False
        if not self.hash_a.verify_password(user.password, hashed_password):
            return False

        return True
