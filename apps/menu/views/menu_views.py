from django.shortcuts import redirect, render
from django.views import View

from apps.menu.forms import FoodForm, MenuForm
from apps.menu.models import Food, Menu


class MenuView(View):
    """
    View for Menu created list
    """

    def get(self, request):
        menus = Menu.objects.all().order_by("-date")
        return render(request, "menu_list.html", {"menus": menus})


class FoodView(View):
    """
    View for Food list
    """

    def get(self, request):
        foods = Food.objects.all()
        return render(request, "foods_list.html", {"foods": foods})


class CreateMenuView(View):
    """
    View for show Menu form and recive form
    """

    def get(self, request):
        form = MenuForm()
        return render(request, "create_menu.html", {"form": form})

    def post(self, request):
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "create_menu.html", {"form": form})


class CreateFoodView(View):
    """
    View for show Food form and recive form
    """

    def get(self, request):
        form = FoodForm()
        return render(request, "create_food.html", {"form": form})

    def post(self, request):
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/food")
        return render(request, "create_food.html", {"form": form})
