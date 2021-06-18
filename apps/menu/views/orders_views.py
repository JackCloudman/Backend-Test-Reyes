from datetime import date, datetime

from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.menu.forms import OrderForm
from apps.menu.models import Menu, MenuOption, Order

from .validations import validate_uuid


class CreateOrderView(View):
    """
    View for show Order form and recive form
    """

    def get(self, request, uuid):
        # VALIDATE UUID
        if not validate_uuid(uuid):
            return redirect("/")

        menu = Menu.objects.filter(uuid=uuid, date=date.today()).first()
        # Menu exist and in time
        if not menu or datetime.now().hour > settings.MAX_ORDER_TIME:
            messages.error(request, "Este menu no esta disponible.")
            return redirect("/")
        # Filter for Menu Options
        menu_options = MenuOption.objects.filter(id_menu=menu)
        form = OrderForm(menu_options)
        context = {"menu": menu, "form": form, "options": menu_options}
        return render(request, "create_order.html", context)

    def post(self, request, uuid):
        # Validate UUID
        if not validate_uuid(uuid):
            return redirect("/")
        # Validation of Menu available
        menu = Menu.objects.filter(uuid=uuid, date=date.today()).first()
        if not menu or datetime.now().hour > settings.MAX_ORDER_TIME:
            messages.error(request, "Orden no creada, este menu no esta disponible.")
            return redirect("/")
        menu_options = MenuOption.objects.filter(id_menu=menu)

        form = OrderForm(menu_options, request.POST)
        # Validation of form
        if form.is_valid():
            form.save()
            messages.success(request, "Orden creada con éxito")
            return redirect("/")
        context = {"menu": menu, "form": form, "options": menu_options}
        return render(request, "create_order.html", context)


class OrdersView(View):
    """
    View for show Order list
    """

    def get(self, request, uuid):
        if not validate_uuid(uuid):
            return redirect("/")
        menu = get_object_or_404(Menu, uuid=uuid)
        orders = Order.objects.filter(selection__id_menu=menu)
        return render(request, "orders_list.html", {"orders": orders})
