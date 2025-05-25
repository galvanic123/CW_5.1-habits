from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Админка модели привычка."""

    list_display = (
        "id",
        "habit",
        "owner",
        "place",
        "start_time",
        "action",
        "is_pleasant",
        "related_habit",
        "periodicity",
        "remuneration",
        "execution_time",
        "is_published",
    )
    search_fields = ("habit",)
    search_filter = ("habit",)