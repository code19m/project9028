from rest_framework import serializers, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models.user import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["current_role"] = serializers.ChoiceField(
            choices=User.Roles.choices, required=False
        )

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        current_role = attrs.get("current_role")
        if len(user.roles) > 1 and current_role is None:
            raise serializers.ValidationError(
                {
                    "keys": "current_role",
                    "roles": user.roles
                },
                code=status.HTTP_400_BAD_REQUEST
            )
        user.current_role = current_role if current_role else user.roles[0]
        user.save()
        data["roles"] = self.user.roles
        data["current_role"] = self.user.current_role
        return data


class MyTokenObtainPairView(TokenObtainPairView):

    def get_serializer_class(self):
        return MyTokenObtainPairSerializer
