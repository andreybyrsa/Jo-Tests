from core.utils.get_field_widgets import get_field_widgets
from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

profile_field_class = "profile-page__input-lighted"


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_picture" ,"username", "first_name", "last_name"]
        labels = {
            "username": "Логин",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "username": get_field_widgets(
                field_class=profile_field_class, placeholder="Ваш логие"
            ),
            "first_name": get_field_widgets(
                field_class=profile_field_class, placeholder="Ваше имя"
            ),
            "last_name": get_field_widgets(
                field_class=profile_field_class, placeholder="Ваша фамилия"
            ),
            "profile_picture": get_field_widgets(
                type="file",
                id="image-input",
                field_class="profile-page__image-input",
            ),
        }

    def save(self, username):
        UserDB = User.objects.get(username=username)
        form_data = self.cleaned_data

        UserDB.username = form_data["username"]
        UserDB.first_name = form_data["first_name"]
        UserDB.last_name = form_data["last_name"]
        UserDB.profile_picture = form_data["profile_picture"]

        UserDB.save()
