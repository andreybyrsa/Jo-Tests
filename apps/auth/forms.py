from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "auth-page__form-input-data",
                "placeholder": "Ваш логин",
            }
        ),
        label="Логин",
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "auth-page__form-input-data",
                "placeholder": "Ваш пароль",
            }
        ),
        label="Пароль",
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "reg-page__form-input-data",
                "placeholder": "Ваш логин",
            }
        ),
        label="Логин",
    )

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "reg-page__form-input-data",
                "placeholder": "Ваше имя",
            }
        ),
        label="Имя",
    )

    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "reg-page__form-input-data",
                "placeholder": "Ваша фамилия",
            }
        ),
        label="Фамилия",
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "reg-page__form-input-data",
                "placeholder": "Ваш пароль",
            }
        ),
        label="Пароль",
    )

    role = forms.ChoiceField(
        choices=(
            ("student", "как студент"),
            ("teacher", "как преподаватель"),
            ("author", "как автор"),
        ),
        widget=forms.Select(
            attrs={
                "id": "selection",
                "class": "reg-page__form-content-links-link",
            }
        ),
    )

    def save(self) -> User:
        form_data = self.cleaned_data

        user = User.objects.create_user(
            username=form_data["username"],
            first_name=form_data["first_name"],
            last_name=form_data["last_name"],
            password=form_data["password"],
            role=form_data['role']
        )

        return user
