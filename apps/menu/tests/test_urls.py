from django.test import SimpleTestCase
from django.urls import resolve, reverse

from apps.menu.views.home_views import HomeView, LoginView, LogoutView, TodayView
from apps.menu.views.menu_views import (
    CreateFoodView,
    CreateMenuView,
    FoodView,
    MenuView,
)
from apps.menu.views.orders_views import CreateOrderView, OrdersView


class TestUrls(SimpleTestCase):
    """
    Class for test the routes
    """

    def setUp(self):
        self.uuid = "00000000-0000-0000-0000-000000000000"

    def test_home_url_is_resolved(self):
        url = reverse("home_view")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_new_order_url_is_resolved(self):
        url = reverse("new_order_view", args=(self.uuid,))
        self.assertEqual(resolve(url).func.view_class, CreateOrderView)

    def test_today_url_is_resolved(self):
        url = reverse("today_view")
        self.assertEqual(resolve(url).func.view_class, TodayView)

    def test_menu_url_is_resolved(self):
        url = reverse("menu_view")
        self.assertEqual(resolve(url).func.view_class, MenuView)

    def test_orders_url_is_resolved(self):
        url = reverse("orders_view", args=(self.uuid,))
        self.assertEqual(resolve(url).func.view_class, OrdersView)

    def test_food_url_is_resolved(self):
        url = reverse("food_view")
        self.assertEqual(resolve(url).func.view_class, FoodView)

    def test_new_menu_url_is_resolved(self):
        url = reverse("create_menu_view")
        self.assertEqual(resolve(url).func.view_class, CreateMenuView)

    def test_new_food_url_is_resolved(self):
        url = reverse("create_food_view")
        self.assertEqual(resolve(url).func.view_class, CreateFoodView)

    def test_login_url_is_resolved(self):
        url = reverse("login_view")
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse("logout_view")
        self.assertEqual(resolve(url).func.view_class, LogoutView)
