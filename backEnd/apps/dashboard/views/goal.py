from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.dashboard.models import Goal
from apps.dashboard.serializers.goal import (
    GoalGetSerializer, GoalCreateSerializer, GoalUpdateSerializer
)

class GoalCreateListView(GenericAPIView):
    queryset = Goal.objects.order_by("-added_time")

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        if Goal.get_current_goal() is not None:
            return Response({
                "error": "Goal for this month already exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def get_serializer_class(self):
        match self.request.method:
            case "GET":
                return GoalGetSerializer
            case "POST":
                return GoalCreateSerializer
            case _:
                raise "Not implemented method"



class GoalRetrieveUpdateView(GenericAPIView):
    queryset = Goal.objects.all()

    def get(self, request, pk):
        goal = self.get_object()
        serializer = self.get_serializer(instance=goal)
        return Response(serializer.data)

    def put(self, request, pk):
        goal = self.get_object()
        serializer = self.get_serializer(instance=goal, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def get_serializer_class(self):
        match self.request.method:
            case "GET":
                return GoalGetSerializer
            case "PUT":
                return GoalUpdateSerializer
            case _:
                raise "Not implemented method"
