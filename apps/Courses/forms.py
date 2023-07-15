from django import forms

from .models import Course

from core.utils.get_field_widgets import get_field_widgets

create_course_input_class = (
    "create-course-page__input create-course-page__input--hidden"
)


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "tests", "groups"]
        labels = {"title": "", "description": "", "tests": "", "groups": ""}
        widgets = {
            "title": get_field_widgets(
                field_class=create_course_input_class, id="course-title"
            ),
            "description": get_field_widgets(
                field_class=create_course_input_class, id="course-description"
            ),
            "tests": get_field_widgets(
                field_class=create_course_input_class, id="course-tests"
            ),
            "groups": get_field_widgets(
                field_class=create_course_input_class, id="course-groups"
            ),
        }
