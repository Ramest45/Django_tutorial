from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.
def thankyou(request):
    return render(request,"enroll/success.html")

def showformate(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email'])
            print('Password:',fm.cleaned_data['password'])
            print('Re-password:',fm.cleaned_data['rpassword'])            

    else:
        fm = StudentRegistration()
        print('Ye Get request se aaya hai')

    return render(request,'enroll/userregistration.html',{'form':fm})
