from datetime import date, datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from apps.menu.models import Menu

# Create your views here.


class HomeView(View):
    """
    View for home page
    """

    def get(self, request):
        context = {"menus": Menu.objects.all()}
        return render(request, "home.html", context)


class TodayView(View):
    """
    View for users that want know the today's menu
    """

    def get(self, request):
        # Filter menu
        menu = Menu.objects.filter(date=date.today()).first()
        # Validation for max order time
        if not menu or datetime.now().hour > settings.MAX_ORDER_TIME:
            messages.error(request, "No hay menu disponible")
            return redirect("/")
        # Redirect to menu URL
        return redirect(f"/menu/{menu.uuid}")


class LoginView(View):
    """
    View for Login
    """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")

    def post(self, request):
        # Get username and password
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Validate authentication
        if user is not None:
            login(request, user)
            return redirect("/")
        # Bad login
        return render(
            request, "login.html", {"message": "Usuario o contraseña incorrectos"}
        )


class LogoutView(View):
    """
    View for logout
    """

    def get(self, request):
        logout(request)
        return redirect("/")
