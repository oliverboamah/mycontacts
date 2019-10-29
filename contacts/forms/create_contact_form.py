from django import forms

from contacts.models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'name', 'email']
        widgets = {
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': 'Enter contact',
                    'class': 'form-control form-control-line',
                    'id': 'phone_number'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name',
                    'class': 'form-control form-control-line',
                    'id': 'name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                    'class': 'form-control form-control-line',
                    'id': 'email'
                }
            ),
        }
