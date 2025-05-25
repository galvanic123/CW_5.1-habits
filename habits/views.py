from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения списка всех привычек"
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для получения конкретной привычки"
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для создания привычки"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для обновления привычки"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_description="Контроллер для удаления привычки"
    ),
)
class HabitViewSet(ModelViewSet):
    """CRUD модели привычка"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_permissions(self):
        """Ограничивает доступ"""
        if self.action in ["retrieve", "update", "destroy"]:
            self.permission_classes = [
                IsOwner | IsAuthenticated,
            ]
        return super().get_permissions()

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class PublicHabitListView(generics.ListAPIView):
    """Список публичных привычек"""

    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination


class HabitsListViewSet(APIView):
    """Список привычек текущего пользователя с пагинацией."""

    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get(self, request):
        habit = Habit.objects.filter(owner=request.user)
        paginated_habit = self.paginated_habit(habit)
        serializer = HabitSerializer(paginated_habit, manu=True)
        return self.get_paginated_response(serializer.data)
