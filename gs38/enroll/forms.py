from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(min_length=5, max_length=50, strip=False, empty_value='Ramest', error_messages={'required':'Enter Your Name'})

    names = forms.CharField()
    
    def clean_name(self):
        valname=self.cleaned_data['names']
        if len(valname)<4:
            raise forms.ValidationError('Enter more than or equal 4 char')
        return valname

    agrees = forms.BooleanField(label_suffix='-', label='I Agree')

    roll = forms.IntegerField(min_value=5, max_value=50)

    price = forms.DecimalField(min_value=5, max_value=40, max_digits=4, decimal_places=2)

    rate = forms.FloatField(min_value=5, max_value=40)

    email = forms.EmailField(max_length=50, min_length=5)

    comment = forms.SlugField()

    website = forms.URLField(min_length=5, max_length=50)

    password = forms.CharField(min_length=5, max_length=50, widget=forms.PasswordInput)

    description = forms.CharField(widget=forms.Textarea)

    feedback = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class':'somecss1 somecss2', 'id':'uniqueid'}))

    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))


