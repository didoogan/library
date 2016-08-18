from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    second_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    image = forms.ImageField()
