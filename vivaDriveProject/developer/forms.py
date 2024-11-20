from django import forms

from .models import Developer
 
class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'first name...'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'last name...'
            }),
        }