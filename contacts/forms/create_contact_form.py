from django import forms

from contacts.models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'name', 'email']
        widgets = {
            'Phone number': forms.TextInput(
                attrs={
                    'placeholder': 'Enter contact',
                    'class': 'form-control form-control-line'
                }
            ),
            'Name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name',
                    'class': 'form-control form-control-line'
                }
            ),
            'Email': forms.Textarea(
                attrs={
                    'placeholder': 'Enter email',
                    'class': 'form-control form-control-line'
                }
            ),
        }