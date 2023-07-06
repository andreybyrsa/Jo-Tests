from django.contrib.auth import get_author_model
from core.utils import get_field_widgets
from django import forms

Author = get_author_model()
profile_field_class = "bottom-side-bar__input"


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["username", "first_name", "last_name", "profile_picture"]
        widgets = {
            "username": get_field_widgets(
                field_class = profile_field_class, placeholder = "Логин"
            ),
            "first_name": get_field_widgets(
                field_class = profile_field_class, placeholder = "Имя"
            ),
            "last_name": get_field_widgets(
                field_class = profile_field_class, placeholder = "Фамилия"
            ),
            "profile_picture": get_field_widgets(
                type = "file",
                id = "image-input",
                field_class = "bottom-side-bar__image-input",
            ),
        }