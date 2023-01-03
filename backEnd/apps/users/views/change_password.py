from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import PasswordField

from apps.users.models import User


class ChangePasswordSerializer(serializers.Serializer):
    old_password = PasswordField()
    new_password = PasswordField()
    new_password_confirm = PasswordField()

    def validate(self, attrs):
        user: User = self.context["user"]
        old_password = attrs["old_password"]
        new_password = attrs["new_password"]
        new_password_confirm = attrs["new_password_confirm"]
        
        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {
                    "keys": "old_password",
                    "details": "incorrect old password"
                }
            )

        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                {
                    "keys": "new_password_confirm",
                    "details": "new_password and new_password_confirm did not match"
                }
            )
        return attrs


class ChangePasswordView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        user: User = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data["new_password"]
        print("PASSWORD", new_password)
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_200_OK)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
