from django import forms
from .models import Placement


class PlacementForm(forms.ModelForm):

    class Meta:

        model = Placement

        fields = [

            "student_name",

            "company_name",

            "job_role",

            "package",

            "placement_date",

            "company_logo",

        ]

        widgets = {

            "placement_date": forms.DateInput(

                attrs={

                    "type": "date"

                }

            ),

        }