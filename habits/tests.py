from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование привычки."""

    def setUp(self):
        """Прописываем тестовые данные привычки."""
        self.user = User.objects.create(email="admin@admin.com")
        self.habit = Habit.objects.create(
            habit="Go out",
            place="Restaurant",
            start_time="2024-12-18T10:54:49Z",
            action="To go out",
            is_pleasant=True,
            periodicity=1,
            execution_time="00:00:60",
            is_published=True,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тест на получение привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        # print(response.json())
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("habit"), self.habit.habit)

    def test_habit_create(self):
        """Тест на создание привычки."""
        url = reverse("habits:habit-list")
        data = {
            "habit": "test",
            "place": "test",
            "start_time": "2024-12-20T10:54:49Z",
            "action": "test",
            "is_pleasant": False,
            "periodicity": 1,
            "execution_time": "00:00:10",
            "is_published": True,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(habit="test").exists())

    # def test_habit_update(self):
    #     """Тест на обновление привычки."""
    #     url = reverse("habits:habit-list", args=(self.habit.pk,))
    #     data = {
    #         "habit": "update test",
    #     }
    #     response = self.client.patch(url, data)
    #     print(response.json())
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("habit"), "update test")

    def test_habit_delete(self):
        """Тест на удаление привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тест список привычек."""
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        print(response.json())
        # data = response.json()
        # result = {
        #     "count": 1,
        #     "next": None,
        #     "previous": None,
        #     "results": [
        #         {
        #             "id": 1,
        #             "habit": "Go out",
        #             "place": "Restaurant",
        #             "start_time": "2024-12-18T10:54:49Z",
        #             "action": "To go out",
        #             "is_pleasant": True,
        #             "periodicity": 1,
        #             "remuneration": None,
        #             "execution_time": "00:01:00",
        #             "is_published": True,
        #             "owner": 1,
        #             "related_habit": None,
        #         }
        #     ],
        # }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(data, result)
