from .models import User
from django.forms import ModelForm, TextInput, PasswordInput, Select


class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": TextInput(
                attrs={
                    "class": "auth-page__form-input-data",
                    "placeholder": "ваш логин",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "auth-page__form-input-data",
                    "placeholder": "ваш пароль",
                }
            ),
        }


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "role"]

        widgets = {
            "username": TextInput(
                attrs={
                    "class": "auth-page__form-input-data",
                    "placeholder": "ваш логин",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "auth-page__form-input-data",
                    "placeholder": "ваше имя",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "auth-page__form-input-data",
                    "placeholder": "ваша фамилия",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "auth-page__form-input-data",
                    "placeholder": "ваш пароль",
                }
            ),
            "role": Select(
                attrs={
                    "class": "auth-page__form-links-link",
                }
            ),
        }
