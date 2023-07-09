from django import forms
from .models import Test


# title =
# description =
# slug = /


class TestCreateForm(forms.Form):
    class Meta:
        model = Test
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": ""}),
            "description": forms.Textarea(attrs={'class': ''}),
        }
    
