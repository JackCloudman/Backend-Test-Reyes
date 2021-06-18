from datetime import date, timedelta

from django.db.utils import IntegrityError
from django.test import TestCase

from apps.menu.models import Food, Menu, MenuOption


class TestViews(TestCase):
    def setUp(self):
        self.uuid = "00000000-0000-0000-0000-000000000000"
        self.food1 = Food.objects.create(name="Sushi", description="")
        self.food2 = Food.objects.create(name="Tacos", description="")
        self.menu = Menu.objects.create(uuid=self.uuid, date=date.today())

    def test_create_duplicated_food(self):
        MenuOption.objects.create(id_menu=self.menu, id_food=self.food1)
        try:
            MenuOption.objects.create(id_menu=self.menu, id_food=self.food1)
            self.fail("Must be unique Menu with Food")
        except IntegrityError:
            pass

    def test_create_duplicated_date_menu(self):
        try:
            Menu.objects.create(date=date.today())
            self.fail("Menu date must be unique")
        except IntegrityError:
            pass

    def test_create_duplicated_uuid_menu(self):
        try:
            tomorrow = date.today() + timedelta(days=1)
            Menu.objects.create(uuid=self.uuid, date=tomorrow)
            self.fail("Menu UUID must be unique")
        except IntegrityError:
            pass
