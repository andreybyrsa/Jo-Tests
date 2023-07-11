from django import forms

from .models import Course

create_course_input_class = "create-course-page__input"


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description"]
        labels = {"title": "", "description": ""}
        widgets = {
            "title": forms.TextInput(attrs={"class": create_course_input_class}),
            "description": forms.TextInput(attrs={"class": create_course_input_class}),
        }
