from django.shortcuts import render
from .forms import Studentregistration
from django.contrib import messages
# Create your views here.
def show_data(request):
    if request.method == "POST":
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request,'Now you can login!!!')
            print(messages.get_level(request))
            messages.debug(request,'This is DEBUG')
            # using this keyword we can change the class of the message
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,'This is New Debug')
            print(messages.get_level(request))
    else:
        fm = Studentregistration()
    return render(request,'enroll/student.html',{'form':fm})