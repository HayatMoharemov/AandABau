from django import forms

from career.models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        exclude = ['is_hired',
                   'submitted_at',
                   'job']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'e.g. David'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'e.g. Davidson'}),
            'email': forms.TextInput(attrs={'placeholder': 'e.g. david_davidson@mail.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g. +4912345678000'})
        }
        job_display = forms.CharField(label='Position', required=False, disabled=True)