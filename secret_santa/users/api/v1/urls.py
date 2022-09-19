from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.api.v1.endpoints.auth import LogoutView, SignInView, SignUpView

auth_urlpatterns = [
    path("signup/", SignUpView.as_view()),
    path("signin/", SignInView.as_view()),
    path("logout/", LogoutView.as_view()),
]

jwt_token_urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns = [
    path("users/auth/", include(auth_urlpatterns)),
    path("token/", include(jwt_token_urlpatterns)),
]
