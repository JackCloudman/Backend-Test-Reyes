# Introduction

What is Corner Menu?
Corner Menu is a system that provides functionalities that facilities to orders meals.

# Background
* Nora manually write to Chilenians what options they have to order today
* Nora should receive multiple messages with Chilenian's orders via WhatsApp, it does not practical
* Whatsapp messages may be forget
* There arent a limit time to select the meal

# Architecture
## Solution design
For the design of the solution, the following stories are raised.
### History 1
Description:
- As: Chilenial user 
- Want: I want to know what is today's menu.
- For: Look for a meal to order

Criteria of acceptance:
- If there is a menu available, you must redirect to the corresponding link.
- If there is no menu available it will show a message that says "There is no menu available"
- A menu will be available if the date is the current day and the time is less than 11 o'clock

### History 2
Description:
- As: Nora 
- Want: I want to create foods
- For: Be able to use them when creating menus

Criteria of acceptance:
- Only Nora must create new foods

### History 3
Description:
- As: Nora 
- Want: I want to create new menus
- For: Have sorted orders by day that are made.

Criteria of acceptance:
- Only Nora must create new menus
- The menu date always be today or future day
- The menu date must be unique
- The menu must have a unique identifier that is an uuid.

### History 4
Description:
- As: Nora 
- Want: I want to get the orders
- For: Have a list and control of orders

Criteria of acceptance:
- Only Nora must list the orders
- Only list the orders by specific date

### History 5
Description:
- As: Chilenial user 
- Want: I want to receive reminder
- For: Place my order on time

Criteria of acceptance:
- The reminder must be async
- It will be sent 1 hour at 10AM
- The notification will be sent to slack channel
## General Architecture diagram
![Alt text](img/architecture.JPG?raw=true "Benefits")

## Pattern design
This section describes the design ideas using the Python programming language and the Django framework.

### The MVT pattern
Django is a popular Python framework, it uses MVT, which stands for Model-Template-View.
* **Model**: It manages the data represented by a database, this contains basically all Entity's information.
* **View**: This receives the HTTP request and has the work to return a respective HTTP response.
* **Template**: It has all visual layers of our application (dynamic HTML)

Here is a simple diagram:
![Alt text](img/mvt.JPG?raw=true "Benefits")

## Implementation standars
Python is a very flexible language so many bad practices can be done that other languages would not allow, so we will use the following standards.

* PEP8: Is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan.
* Flake8: Is a command-line utility for enforcing style consistency across Python projects. By default it includes lint checks provided by the PyFlakes project, PEP-0008 inspired style checks.
* iSort: Is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type
* Black: Is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting

## What are the benefits of the new System?
![Alt text](img/benefits.JPG?raw=true "Benefits")

# Implementation
## Models
In the project we have the following entities

![Alt text](img/er.JPG?raw=true "Benefits")
### Food
Model that contain info about food
|Field|Type|Description|
|---|---|---|
|name|string|Name of food, max lenght 50 characters|
|description|string|A description of food max 255 characters|

### Menu
Model that contain info about menu
|Field| Type| Description|
|---|---|---|
|uuid|uuid4|A unic identifier based in uuid4, automaticaly added|
|date|Date|Date of the menu, must be unique|
|foods|QuerySet|A M2M relationship that contains all foods that have the menu|
### MenuOption
Model that contain relationship between Menu and food,the relationship must be unique
|Field| Type| Description|
|---|---|---|
|id_menu|Menu|Menu object|
|id_food|Food|Food object|
### Order
Model that contain information about Order
|Field| Type| Description|
|---|---|---|
|username|string|User that order, max_length 50|
|selecion|MenuOption|A unique food selection|
|comments|string|A extra field for extra comments in your order|
### Tests
|Name| Description|
|---|---|
|test_create_duplicated_food|Test try to create two MenuOption for same menu and food|
|test_create_duplicated_date_menu|Test for menu with same date|
|test_create_duplicated_uuid_menu|Test for menu with same uuid|
|test_create_duplicated_uuid_menu|Test for menu with same uuid|
## Views
The views are separated into
### Home Views
|Class| HTTP Method|Description|Authentication|
|---|---|---|---|
|HomeView|GET|View for home page|No|
|TodayView|GET|View to redirect if exist available today's menu|No|
|LoginView|GET|View that return rendered login page|No|
|LoginView|POST|View that recive information of login|No|
|LoginView|GET|View that recive information of login|No|
|LogoutView|GET|View for logout|Yes|
### Menu Views
|Class| HTTP Method|Description|Authentication|
|---|---|---|---|
|MenuView|GET|View for menu list|Yes|
|FoodView|GET|View for food list|Yes|
|CreateMenuView|GET|View for create new menu|Yes|
|CreateMenuView|POST|View that recive information of MenuForm|Yes|
|CreateFoodView|GET|View for create new food|Yes|
|CreateFoodView|POST|View that recive information of FoodForm|Yes|
### Orders View
|Class| HTTP Method|Description|Authentication|
|---|---|---|---|
|CreateOrderView|GET|View for create new Order|No|
|CreateOrderView|POST|View that recive information of OrderForm|No|
|OrdersView|GET|View for orders list|Yes|

### Tests
|Name| Description|
|---|---|
|test_home_view_get|Test home page and rendered template|
|test_menu_view_get|Test menu list view authentication|
|test_orders_view|Test order list view authentication|
|test_today_view|Test http code response if exist available menu|
|test_new_menu_view|Test create new menu view authentication|
|test_new_food_view|Test create new food view authentication|
## URLs
|Name| Path |View| Autentication|
|---|---|---|---|
|menu_view|menu|MenuView|Yes|
|orders_view|menu/\<str:uuid\>/orders|OrdersView|Yes|
|food_view|food|FoodView|Yes|
|create_menu_view|menu/new|CreateMenuView|Yes|
|create_food_view|food/new|CreateFoodView|Yes|
|home_view|--|HomeView|No|
|new_order_viewview|menu/\<str:uuid\>|CreateOrderView|No|
|today_view|today|TodayView|No|
|login_view|login|LoginView|No|
|logout_view|logout|LogoutView|No|
### Tests
|Name| Description
|---|---|
|test_home_url_is_resolved|Test if resolve "home_view"|
|test_new_order_url_is_resolved|Test if resolve "new_order_view"|
|test_today_url_is_resolved|Test if resolve "today_view"|
|test_menu_url_is_resolved|Test if resolve "menu_view"|
|test_orders_url_is_resolved|Test if resolve "orders_view"|
|test_food_url_is_resolved|Test if resolve "food_view"|
|test_new_menu_url_is_resolved|Test if resolve "create_menu_view"|
|test_new_food_url_is_resolved|Test if resolve "create_food_view"|
|test_login_url_is_resolved|Test if resolve "login_view"|
|test_logout_url_is_resolved|Test if resolve "logout_view"|
## Templates

|Name| Description|
|---|---|
|base.html|The layout of all templates|
|create_food.html|Template for new food|
|create_menu.html|Template for new menu|
|create_order.html|Template for new order|
|foods_list.html|Template for food list|
|menu_list.html|Template for menu list|
|orders_list.html|Template for orders list|
|home.html|Template for home page|
|login.html|Template for login form|

## Screenshots

Home page
![Alt text](img/home.JPG?raw=true "Home")
Create order
![Alt text](img/new_order.JPG?raw=true "New order")
Menu list
![Alt text](img/menu_list.JPG?raw=true "Menu List")
Orders list
![Alt text](img/order_list.JPG?raw=true "Orders List")
Create Menu
![Alt text](img/new_menu.JPG?raw=true "New Menu")
Create Food
![Alt text](img/new_food.JPG?raw=true "New food")
