from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def start_time_reminder():
    """Отправляет напоминание пользователю о начале выполнения привычки на почту или в TG."""     # noqa
    today = timezone.now().today()
    message = "Пришло время начать выполнять привычку!"
    habits = Habit.objects.filter(owner__isnull=False, start_time=today)

    for habit in habits:
        if habit.owner.tg_chat_id:
            send_telegram_message(message)
