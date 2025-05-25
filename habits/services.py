import requests


def send_telegram_message(chat_id, message):
    """Функция отправки уведомлений в TG"""
    params = {"text": message, "chat_id": chat_id}
    requests.get(
        "{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params           # noqa
    )
