from config import settings
import requests


def send_telegram_message(message, tg_chat_id):
    """Функция отправки уведомлений в TG"""
    params = {
        "text": message,
        "tg_chat_id": tg_chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params,           # noqa
    )