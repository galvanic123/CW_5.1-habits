import os

import telebot
from django.core.management import BaseCommand

API_KEY = os.getenv("TELEGRAM_TOKEN")
MY_ID = os.getenv("TELEGRAM_MY_ID")


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(API_KEY)
        message = "Тестовое сообщение"

        try:
            response = bot.send_message(chat_id=MY_ID, text=message)        # noqa
        except Exception as e:
            print(e)
