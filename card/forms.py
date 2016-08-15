from django import forms
from books.models import Book


# class CardForm(forms.ModelForm):
#     class Meta:
#         model = Card
#         fields = ['books']
# widgets = {'books': forms.RadioSelect}

# def __init__(self, *args, **kwargs):
#     super(CardForm, self).__init__(self, *args, **kwargs)
#     self.fields['books'].queryset = Book.objects.filter(is_taken=False)

# def __init__(self, *args, **kwargs):
#     super(CardForm, self).__init__(self, *args, **kwargs)
#     self.fields['books'] = forms.ModelChoiceField(queryset=Book.objects.filter(is_taken=False))


class CardForm(forms.Form):
    books = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['books'].choices = [(o.id, o.title) for o in Book.objects.filter(is_taken=False)]
