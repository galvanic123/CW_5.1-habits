from datetime import timedelta

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычки."""


    habit = models.CharField(max_length=255, verbose_name="Привычка", **NULLABLE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Автор привычки",
        help_text="Укажите автора привычки",
        related_name="users_habits",
        **NULLABLE
    )
    place = models.CharField(
        max_length=255, verbose_name="Место выполнения привычки", **NULLABLE
    )
    start_time = models.DateTimeField(
        verbose_name="Время старта",
        help_text="Выберете время когда необходимо выполнять привычку",
        **NULLABLE
    )
    action = models.CharField(
        max_length=300,
        verbose_name="Действие привычки",
        help_text="Укажите действие привычки",
        **NULLABLE
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Привычка является приятной",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        related_name="related_habits",
        **NULLABLE
    )

    periodicity = models.PositiveIntegerField(
        verbose_name="Периодичность выполнения привычки в неделю",
        help_text="Укажите переодичность выполнения привычки",
    )
    remuneration = models.CharField(
        verbose_name="Вознаграждение после выполнения привычки", **NULLABLE
    )
    execution_time = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Время выполнения привычки",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Публикация в общем доступе",
        help_text="Опубликовать для общего доступа",
    )

    def __str__(self):
        return f"{self.action} by {self.owner.username} at {self.place}"

    