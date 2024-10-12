from django.shortcuts import render
from .forms import Studentregistration
from django.contrib import messages
# Create your views here.
def show_data(request):
    if request.method == "POST":
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your database updated successfully!!!')
            messages.info(request, 'You can now login your account')
            fm = Studentregistration()
    else:
        fm = Studentregistration()
    return render(request,'enroll/student.html',{'form':fm})