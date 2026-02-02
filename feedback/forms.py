from django import forms

from feedback.models import CreateFeedback

class CreateFeedbackForm(forms.ModelForm):

    model = CreateFeedback

    fields = '__all__'
    widgets = {
        'first_name': forms.TextInput(attrs={'placeholder': 'e.g. David'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'e.g. Davidson'}),
    }