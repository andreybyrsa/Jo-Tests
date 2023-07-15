from django import forms
from .models import Test

from core.utils.get_field_widgets import get_field_widgets

create_test_input_class = "create-test-page__input create-test-page__input--hidden"


class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ["title", "description"]
        labels = {"title": "", "description": ""}
        widgets = {
            "title": get_field_widgets(
                field_class=create_test_input_class, id="test-title"
            ),
            "description": get_field_widgets(
                field_class=create_test_input_class, id="test-descriprion"
            ),
        }
