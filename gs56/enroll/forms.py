from django import forms
from .models import User

class Studentregistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Student_name','email','password']


class Teacherregistration(Studentregistration):
    class Meta(Studentregistration.Meta):
        fields = ['Teacher_name','email','password']