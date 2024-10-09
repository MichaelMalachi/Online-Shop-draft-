from django import forms
from product.models import CustomUser123
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser123  # Используем кастомную модель пользователя
        fields = ['username', 'email', 'password1', 'password2']
