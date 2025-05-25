from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тестирование пользовательских данных."""

    def setUp(self):
        """Прописываем тестовые данные пользователя."""
        self.user = User.objects.create(
            email="admin@admin.com",
            password="123qwe",
            phone="89999999999",
            tg_nik="test",
            tg_chat_id="test",
        )
        self.client.force_authenticate(user=self.user)
        self.assertIsNotNone(self.user.pk)

    def test_user_create(self):
        """Тест на создание пользователя."""
        url = reverse("users:users-list")
        data = {
            "email": "test@test.com",
            "password": "test123",
            "phone": "test",
            "tg_nik": "test",
            "tg_chat_id": "12345",
        }
        response = self.client.post(url, data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.count(), 2)

    def test_list_users(self):
        """Тест на получение списка пользователей."""

        url = reverse("users:users-list")
        response = self.client.get(url)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_retrieve(self):
        """Тест на получение пользователя."""
        url = reverse("users:users-detail", args=(self.user.pk,))
        response = self.client.get(url)
        # print(response.json())
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), self.user.email)

    def test_user_update(self):
        """Тест на обновление пользователя."""
        url = reverse("users:users-detail", args=(self.user.pk,))
        data = {"email": "admin_test@admin.com"}
        response = self.client.patch(url, data)
        # print(response.json())
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), "admin_test@admin.com")

    def test_user_delete(self):
        """Тест на удаление пользователя."""
        url = reverse("users:users-detail", args=(self.user.pk,))
        response = self.client.delete(url)
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
