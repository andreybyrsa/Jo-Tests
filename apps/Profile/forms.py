from apps.Courses.models import Group
from core.utils.get_field_widgets import get_field_widgets
from django import forms

from django.contrib.auth import get_user_model

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

    def save(self, username):
        UserDB = User.objects.get(username=username)
        form_data = self.cleaned_data

        UserDB.username = form_data["username"]
        UserDB.first_name = form_data["first_name"]
        UserDB.last_name = form_data["last_name"]
        UserDB.profile_picture = form_data["profile_picture"]

        UserDB.save()


class FindGroupStudentForm(forms.Form):
    group_name = forms.CharField(
        label="Название группы",
        widget=forms.TextInput(attrs={"placeholder": "Введите название группы"}),
    )
    student_login = forms.CharField(
        label="Логин студента",
        widget=forms.TextInput(attrs={"placeholder": "Введите логин студента"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        group_name = cleaned_data.get("group_name")
        student_login = cleaned_data.get("student_login")

        try:
            user = User.objects.get(username=student_login)
        except User.DoesNotExist:
            raise forms.ValidationError("Student not found.")

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            raise forms.ValidationError("Group not found.")

        cleaned_data["group"] = group
        cleaned_data["student"] = user

        return cleaned_data


class GroupEditForm(forms.Form):
    group_name = forms.CharField(
        label="Название группы",
        widget=forms.TextInput(attrs={"placeholder": "Введите название группы"}),
    )
    student_login = forms.CharField(
        label="Добавить студента",
        widget=forms.TextInput(attrs={"placeholder": "Введите логин студента"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group = None
        self.student = None

    def clean_group_name(self):
        group_name = self.cleaned_data["group_name"]
        try:
            self.group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            raise forms.ValidationError("Group not found.")
        return group_name

    def clean_student_login(self):
        student_login = self.cleaned_data["student_login"]
        try:
            self.student = User.objects.get(username=student_login)
        except User.DoesNotExist:
            raise forms.ValidationError("Student not found.")
        return student_login

    def save(self):
        if self.group is None or self.student is None:
            return

        if self.student in self.group.user_set.all():
            self.group.user_set.remove(self.student)
        else:
            self.group.user_set.add(self.student)
