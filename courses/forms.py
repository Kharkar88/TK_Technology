from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:

        model = Course

        fields = [
            "name",
            "category",
            "duration",
            "fees",
            "description",
            "image",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "category": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "duration": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "fees": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),
        }