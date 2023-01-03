from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User


class ChangeRoleSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=User.Roles.choices)

    def validate(self, attrs):
        user = self.context["user"]
        role = attrs["role"]
        if role not in user.roles:
            raise serializers.ValidationError(
                {
                    "keys": "role",
                    "details": f"user is not {role}"
                }
            )
        return attrs


class ChangeRoleView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeRoleSerializer

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        role = serializer.validated_data["role"]
        user.current_role = role
        user.save()
        return Response(status=status.HTTP_200_OK)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
