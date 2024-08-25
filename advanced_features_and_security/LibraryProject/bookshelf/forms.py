from django import forms

class ExampleForm(forms.Form):
    nama = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label="email")
    massage = forms.CharField(widget=forms.Textarea, label="Your massage")


class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)