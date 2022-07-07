from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.v1.serializers import UserSignUpSerializer
from users.services.auth_service import auth_service


class SignUpView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UserSignUpSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = auth_service.signup_user(serializer.data)

        return Response({"user_id": user.pk})


class SignInView(ObtainAuthToken):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        return Response(
            {
                "user_id": user.pk,
            }
        )


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(status=status.HTTP_200_OK)
