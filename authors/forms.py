from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}), label='First name :')
    num = forms.IntegerField(initial=777, label="Steps")
    output = forms.CharField(widget=forms.Textarea(attrs={'id': 'result-text', 'disabled': True}), label='')