from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Ramest",help_text="Is field me 30 character hi likh skte hai")
    email = forms.EmailField(initial="ramestgupta1234@gmail.com")
    first_name=forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput())