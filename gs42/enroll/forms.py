from django import forms
from django.core import validators


class StudentRegistration(forms.Form):
    name=forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned_data = super().clean()
        Password = self.cleaned_data['password']
        Repassword = self.cleaned_data['rpassword']
        if(Password!=Repassword):
            raise forms.ValidationError('Password Must be similar to the repassword field')
