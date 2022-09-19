from users.models import User


class AuthService:
    def signup_user(self, user_sign_up_data: dict) -> User:
        email = user_sign_up_data["email"]
        password = user_sign_up_data["password1"]
        name = user_sign_up_data["name"]

        user: User = User.objects.create_user(email=email, password=password, name=name)

        return user


auth_service = AuthService()
