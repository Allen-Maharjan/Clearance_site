from django.db import models
from django import forms


class Login(forms.Form):

    name = forms.CharField(min_length=5, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        print(self.cleaned_data)
