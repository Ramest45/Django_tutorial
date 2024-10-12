from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(label='Your Name',label_suffix='-',initial='Ramest',required=False, disabled=True, help_text='Limit 20 Chars')