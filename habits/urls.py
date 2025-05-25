from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitsListViewSet, HabitViewSet, PublicHabitListView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"habit", HabitViewSet, basename="habit")

urlpatterns = [
    path("habits/public/", PublicHabitListView.as_view(), name="public-habit-list"),
    path("habits-list/", HabitsListViewSet.as_view(), name="habits-list"),
] + router.urls
