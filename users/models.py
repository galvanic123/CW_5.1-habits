from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель пользователя."""

    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", help_text="Укажите телефон", **NULLABLE         # noqa
    )
    tg_nik = models.CharField(
        max_length=50, verbose_name="TG", help_text="Укажите TG ник", **NULLABLE    # noqa
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Укажите аватар",
        **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="TG chat_id",
        help_text="Укажите TG chat_id",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email
