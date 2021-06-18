from django.contrib.auth.decorators import login_required
from django.urls import path

from .views.home_views import HomeView, LoginView, LogoutView, TodayView
from .views.menu_views import CreateFoodView, CreateMenuView, FoodView, MenuView
from .views.orders_views import CreateOrderView, OrdersView

urlpatterns = [
    # Nora's routes
    path("menu", login_required(MenuView.as_view()), name="menu_view"),
    path(
        "menu/<str:uuid>/orders",
        login_required(OrdersView.as_view()),
        name="orders_view",
    ),
    path("food", login_required(FoodView.as_view()), name="food_view"),
    path("menu/new", login_required(CreateMenuView.as_view()), name="create_menu_view"),
    path("food/new", login_required(CreateFoodView.as_view()), name="create_food_view"),
    # Common routes
    path("", HomeView.as_view(), name="home_view"),
    path("menu/<str:uuid>", CreateOrderView.as_view(), name="new_order_view"),
    path("today", TodayView.as_view(), name="today_view"),
    # Login/Logout routes
    path("login", LoginView.as_view(), name="login_view"),
    path("logout", login_required(LogoutView.as_view()), name="logout_view"),
]
