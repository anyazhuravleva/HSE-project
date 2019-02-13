from django import forms


class DataForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    tick = forms.BooleanField()
    text = forms.CharField()