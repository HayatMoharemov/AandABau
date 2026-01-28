from django import forms

from contact.models import ContactForm


class ContactFormModel(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'e.g. David'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'e.g. Davidson'}),
            'email': forms.TextInput(attrs={'placeholder': 'e.g. david_davidson@mail.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g. +4912345678000'})
        }
