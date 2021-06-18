from datetime import date, timedelta

from django.test import TestCase

from apps.menu.forms import FoodForm, MenuForm, OrderForm
from apps.menu.models import Food, Menu, MenuOption


class TestForms(TestCase):
    """
    Class for Test the forms
    """

    def setUp(self):
        # Foods
        self.food1 = Food.objects.create(name="Sushi", description="")
        self.food2 = Food.objects.create(name="Tacos", description="")
        self.food3 = Food.objects.create(name="Wings", description="")
        self.food4 = Food.objects.create(name="Hamburguer", description="")
        # Menu
        self.today = date.today()
        self.future_day = self.today + timedelta(days=364)
        self.menu = Menu.objects.create(date=self.future_day)
        # Option
        self.option1 = MenuOption.objects.create(id_menu=self.menu, id_food=self.food1)

    def test_menu_form_valid_date(self):
        future_day = self.today + timedelta(days=365)
        form = MenuForm(
            data={
                "date_month": future_day.month,
                "date_day": future_day.day,
                "date_year": future_day.year,
                "foods": [self.food1.id],
            }
        )
        self.assertTrue(form.is_valid())

    def test_menu_form_no_valid(self):
        yesterday = self.today - timedelta(days=1)
        form = MenuForm(
            data={
                "date_month": yesterday.month,
                "date_day": yesterday.day,
                "date_year": yesterday.year,
                "foods": ["-1"],
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_food_form_valid(self):
        form = FoodForm(data={"name": "Ramen", "description": "Traditional ramen"})
        self.assertTrue(form.is_valid())

    def test_food_form_no_valid(self):
        form = FoodForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_order_form_valid(self):
        form = OrderForm(
            menu_options=MenuOption.objects.filter(id_menu=self.menu),
            data={
                "username": "JackCloudman",
                "selection": self.option1.id,
                "comments": "Salmon sushi please",
            },
        )
        self.assertTrue(form.is_valid())

    def test_order_form_no_valid_option(self):
        form = OrderForm(
            menu_options=MenuOption.objects.filter(id_menu=self.menu),
            data={
                "username": "JackCloudman",
                "selection": "-1",
            },
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_order_form_no_data(self):
        form = OrderForm(
            menu_options=MenuOption.objects.filter(id_menu=self.menu),
            data={},
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
