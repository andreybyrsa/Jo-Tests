from models import Teacher
from core.utils.get_field_widgets import get_field_widgets
from django import forms

profile_field_class = "bottom-side-bar__input"


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
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
    def save(self, user_id):
        TeacherDB = Teacher.objects.get(user_id=user_id)
        form_data = self.cleaned_data

        TeacherDB.username = form_data["username"]
        TeacherDB.first_name = form_data["first_name"]
        TeacherDB.last_name = form_data["last_name"]
        TeacherDB.profile_picture = form_data["profile_picture"]

        TeacherDB.save()