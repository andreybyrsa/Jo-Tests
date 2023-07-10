from django import forms
from .models import Test


# title =
# description =
# slug = /

create_test_input_class = "create-test-page__input create-test-page__input--hidden"


class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ["title", "description"]
        labels = {"title": "", "description": ""}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": create_test_input_class, "id": "test-title"}
            ),
            "description": forms.Textarea(
                attrs={"class": create_test_input_class, "id": "test-descriprion"}
            ),
        }
