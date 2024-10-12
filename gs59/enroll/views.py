from django.shortcuts import render
from .forms import Studentregistration
from django.contrib import messages
# Create your views here.
def show_data(request):
    messages.info(request,'Now You can Login')
    messages.success(request,'Now You start the app')
    messages.warning(request,'this is warning alarm')
    messages.error(request,'this is an error msg')
    fm = Studentregistration()
    return render(request,'enroll/student.html',{'form':fm})