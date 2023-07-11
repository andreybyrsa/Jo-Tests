from django import forms

from .models import Course

create_course_input_class = (
    "create-course-page__input create-course-page__input--hidden"
)


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description"]
        labels = {"title": "", "description": ""}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": create_course_input_class, "id": "course-title"}
            ),
            "description": forms.TextInput(
                attrs={"class": create_course_input_class, "id": "course-description"}
            ),
        }
