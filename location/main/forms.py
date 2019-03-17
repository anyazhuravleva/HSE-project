from django import forms
from main.models import AntennasTable as AT


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class RegForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class DataForm(forms.Form):
    file = forms.FileField(required=True)
    antenna = forms.ModelChoiceField(queryset=AT.objects.all(), required=True)


class AntennasForm(forms.Form):
    antennas = forms.FileField(required=True)
