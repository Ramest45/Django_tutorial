from django import forms
from django.core import validators


class StudentRegistration(forms.Form):
    #jb hme css pure ek input box pr apply krna ho tb ise use krte hai.
    error_css_class = 'error'
    
    name=forms.CharField(error_messages={'required':'Enter your Name'})
    email = forms.EmailField(error_messages={'required':'Enter your Email'},min_length=5, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your Password'},min_length=5, max_length=50)