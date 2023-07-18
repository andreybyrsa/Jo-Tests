from apps.Courses.models import Group
from core.utils.get_field_widgets import get_field_widgets
from django import forms

from django.contrib.auth import get_user_model

from apps.Courses.models import Group

User = get_user_model()

profile_field_class = "profile-modal__input--lighted"


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_picture", "username", "first_name", "last_name"]
        labels = {
            "username": "Логин",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "profile_picture": "",
        }
        widgets = {
            "username": get_field_widgets(
                field_class=profile_field_class, placeholder="Новый логин"
            ),
            "first_name": get_field_widgets(
                field_class=profile_field_class, placeholder="Новое имя"
            ),
            "last_name": get_field_widgets(
                field_class=profile_field_class, placeholder="Новая фамилия"
            ),
            "profile_picture": get_field_widgets(
                type="file",
                id="image-input",
                field_class="profile-modal__image-input",
            ),
        }

    def save(self, id):
        UserDB = User.objects.get(id=id)
        form_data = self.cleaned_data

        UserDB.username = form_data["username"]
        UserDB.first_name = form_data["first_name"]
        UserDB.last_name = form_data["last_name"]
        UserDB.profile_picture = form_data["profile_picture"]

        UserDB.save()


class GroupStudentForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["groupname"]
        labels = {
            "groupname": "Название группы"
        }
        widgets = {
            "groupname": get_field_widgets(
                    field_class= "profile-page__input-lighted",
                    placeholder= "Введите название группы",
                    id= 'group-input'
                ),
        }
