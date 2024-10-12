from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(widget=forms.PasswordInput)
    # middlename=forms.CharField(widget=forms.HiddenInput)
    # comment=forms.CharField(widget=forms.Textarea)
    age=forms.CharField(widget=forms.CheckboxInput)
    file=forms.CharField(widget=forms.FileInput)
    text1 = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1', 'id':'uniqueid'}))