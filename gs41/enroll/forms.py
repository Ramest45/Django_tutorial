from django import forms
from django.core import validators

# use of custom validators in django
def start_with_s(value):
    if(value[0]!='r'):
        raise forms.ValidationError('Name should be start with r')

class StudentRegistration(forms.Form):
    # custom validators in django
    name=forms.CharField(validators=[start_with_s])
    # built-in validators in django
    email = forms.EmailField(validators=[validators.MaxLengthValidator(25)])



    # validating complete form at once
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname)<4:
    #         raise forms.ValidationError('Name should be more than or equal to 4')
    #     if len(valemail)<10:
    #         raise forms.ValidationError('Email should be more than or equal to 10')

