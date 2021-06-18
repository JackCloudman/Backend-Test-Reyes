from datetime import date, datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from apps.menu.models import Menu


class TestViews(TestCase):
    """
    Class for Test the views
    """

    def setUp(self):
        self.uuid = "00000000-0000-0000-0000-000000000000"
        self.menu = Menu.objects.create(uuid=self.uuid, date=date.today())
        # Logged user
        self.user = get_user_model().objects.create_user(
            username="test", email=None, password="test"
        )
        client = Client()
        client.login(username="test", password="test")
        self.loged_client = client
        self.client = Client()

    def test_home_view_get(self):
        response = self.client.get(reverse("home_view"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_menu_view_get(self):
        url = reverse("menu_view")
        # No logged
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Logged user
        response = self.loged_client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_orders_view(self):
        url = reverse("orders_view", args=[self.uuid])
        # No logged
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Logged user
        response = self.loged_client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_today_view(self):
        url = reverse("today_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        if datetime.now().hour > settings.MAX_ORDER_TIME:
            self.assertRedirects(response, "/")
        else:
            self.assertRedirects(response, f"/menu/{self.uuid}")

    def test_new_menu_view(self):
        url = reverse("create_menu_view")
        # No logged
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Logged user
        response = self.loged_client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_food_view(self):
        url = reverse("create_food_view")
        # No logged
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Logged user
        response = self.loged_client.get(url)
        self.assertEqual(response.status_code, 200)
