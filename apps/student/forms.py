<<<<<<< HEAD:apps/author/forms.py
from core.utils import get_field_widgets
from django import forms
from models import Author
=======
from core.utils.get_field_widgets import get_field_widgets
from django import forms
from models import Student
>>>>>>> task#student:apps/student/forms.py

profile_field_class = "bottom-side-bar__input"


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Student
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
        StudentDB = Student.objects.get(user_id=user_id)
        form_data = self.cleaned_data

        StudentDB.username = form_data["username"]
        StudentDB.first_name = form_data["first_name"]
        StudentDB.last_name = form_data["last_name"]
        StudentDB.profile_picture = form_data["profile_picture"]

        StudentDB.save() 