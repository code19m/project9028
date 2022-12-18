from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User


class CurrentUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "image",
            "phone_number",
            "roles"
        )
        read_only_fields = ("username", "roles")


class CurrentUserViewSet(
    GenericAPIView
):
    serializer_class =  CurrentUserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer: CurrentUserSerializer = self.get_serializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
