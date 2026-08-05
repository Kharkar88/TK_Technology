from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [

            'student',
            'amount',
            'transaction_id',
            'status',

        ]

        widgets = {

            'student': forms.Select(attrs={
                'class': 'form-control'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Amount'
            }),

            'transaction_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Transaction ID'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),

        }