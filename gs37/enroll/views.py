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
            # print(fm)
            # print('Ye POST Request se aaya hai')
            print('Form Validated')
            print('Clean Data', fm.cleaned_data)
            Name = fm.cleaned_data['name']
            Email = fm.cleaned_data['email']
            Password =  fm.cleaned_data['password']
            print('Name',Name)
            print('Email',Email)
            print('Password',Password)
            return HttpResponseRedirect('/reg/thanks')
            #return render(request,"enroll/success.html",{'nm':Name})
            #fm = StudentRegistration()   # ye use isliye kr rhe taki submit krne ke baar hmara field khali ho jai

    else:
        fm = StudentRegistration()
        print('Ye Get request se aaya hai')

    return render(request,'enroll/userregistration.html',{'form':fm})
