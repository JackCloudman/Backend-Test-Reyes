import datetime

from django import forms

from .models import Food, Menu, Order


class MenuForm(forms.ModelForm):
    """
    Description: Form class to create new Menu
    Fields:
        Date: Menu's date, must be today or future day
        Foods: Check box of selections foods for the menu, must be at least one
    """

    date = forms.DateField(widget=forms.SelectDateWidget())
    foods = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(), widget=forms.CheckboxSelectMultiple()
    )

    def clean_date(self):
        """
        Description: Method to validate date of menu
        """

        date = self.cleaned_data["date"]
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    class Meta:
        model = Menu
        fields = ("date", "foods")


class OrderForm(forms.ModelForm):
    """
    Description: Form class to create new Order
    Fields:
        Username: Name / email for user that can order,
                  in the future should be added automatically.
        Selection: Menu options linked to menu of day
        Comments: A extra field to add comment for your selection
    """

    def __init__(self, menu_options, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)  # populates the post
        # Filter menu options
        self.fields["selection"].queryset = menu_options
        self.fields["selection"].label = "Platillo"
        self.fields["comments"].label = "Comentarios adicionales"

    class Meta:
        model = Order
        fields = ("username", "selection", "comments")


class FoodForm(forms.ModelForm):
    """
    Description: Form class to create new Food
    Fields:
        Name: Food's name
        Description: A description of food
    """

    class Meta:
        model = Food
        fields = ("name", "description")
