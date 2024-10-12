from django.core import validators
from django import forms
from .models import User
class StudentRegistration(forms.ModelForm):
 # to use validators
 name = forms.CharField(max_length=50,required=False)
 class Meta:
  model = User
  fields = ['name', 'email', 'password']
  labels = {'name':'Enter Name','password':'Enter Password','email':'Enter Email'}
  help_text = {'name':'Enter Your Full Name'}
  error_messages = {'name':{'required':'Naam likhna jaruri hai'},
               'password':{'required':'Password likhna jaruri hai'}}
  widgets = {'password':forms.PasswordInput,
             'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Yaha Naam Likhe'})}

