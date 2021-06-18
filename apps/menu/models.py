from uuid import uuid4

from django.db import models


# Create your models here.
class Food(models.Model):
    """
    Decription: Class that contain info about food
    Fields:
        Name: Name of food, max lenght 50 characters
        Description: A description of food max 255 characters
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    """
    Decription: Class that contain info about menu
    Fields:
        UUID: A unic identifier based in uuid4, automaticaly added
        Date: Date of the menu, must be unique
        Foods: A M2M relationship that contains all foods that have the menu
    """

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    date = models.DateField(unique=True)
    foods = models.ManyToManyField(Food, through="MenuOption")

    def __str__(self):
        return f"{self.date}"


class MenuOption(models.Model):
    """
    Description: Class that contain relationship between Menu and food,
        the relationship must be unique
    Fields:
        id_menu: Menu object
        id_food: Food object
    """

    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    id_food = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("id_menu", "id_food"),)

    def __str__(self):
        return f"{self.id_food}"


class Order(models.Model):
    """
    Description: Class that contain information about Order
    Fields:
        Username: User that order, max_length 50
        Selection: A unique food selection
        Comments: a extra field for extra comments in your order
    """

    username = models.CharField(max_length=50)
    selection = models.ForeignKey(MenuOption, on_delete=models.CASCADE)
    comments = models.CharField(max_length=100, blank=True)
