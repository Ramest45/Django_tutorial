from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm = StudentRegistration()
    return render(request,'enroll/userregistration3.html',{'form':fm})
    # fm.order_fields(field_order=['email','name','first_name'])
    # return render(request,'enroll/userregistration2.html',{'form':fm})
    # return render(request,'enroll/userregistration.html',{'form':fm})
    # fm = StudentRegistration(auto_id='some_%s', label_suffix='-',initial={'name':'Ram', 'email':'sita@gmail.com'})