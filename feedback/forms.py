from django import forms

from feedback.models import CreateFeedback

class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = CreateFeedback

        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'e.g. David'}),
        }