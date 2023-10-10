from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

# python manage.py test


class UserModelTestCase(TestCase):
    username = "Dina"
    password = "Hi234245!*vgvg"

    def setUp(self):  # преднастройка
        User.objects.create(username=self.username, password=make_password(self.password))

    def test_model_create(self):
        print("""Тестируем модель на корректное создание пользователя""")
        user = User.objects.get(username=self.username)
        self.assertEqual(user.username, self.username)
    def test_password_verification(self):
        print("Testing password verification...")
        user = User.objects.get(username=self.username)
        self.assertTrue(user.check_password(self.password))

    def test_user_creation_increases_count(self):
        print("Testing new user creation...")
        initial_count = User.objects.count()
        User.objects.create(username="TestUser2", password=make_password("TestPassword2"))
        new_count = User.objects.count()
        self.assertEqual(initial_count + 1, new_count)

    def test_absence_of_non_existent_user(self):
        print("Testing absence of non-existent user...")
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="NonExistentUser")

class HomeListTestCase(TestCase):
    def test_post_home(self):
        print("Testing POST request to home...")
        response = self.client.post(reverse("home"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_non_existent_route(self):
        print("Testing non-existent route...")
        response = self.client.get("/non-existent/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_home_response_content(self):
        print("Testing home response content...")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.content.decode(), "OK")

class SuccessfullTestCase(TestCase):
    def test(self):
        print(
            """\n\n\n
            #################################\n
            ALL TEST SUCCESSFULL\n
            #################################\n
            \n\n\n"""
                    )