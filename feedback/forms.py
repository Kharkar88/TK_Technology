from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:

        model = Feedback

        fields = [
            "rating",
            "message",
        ]

        widgets = {

            "rating": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Write your feedback..."
                }
            ),

        }