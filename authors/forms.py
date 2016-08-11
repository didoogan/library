from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='First name :')
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last name :')

    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
