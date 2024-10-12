from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showformdata(request):
 fm = StudentRegistration()
 return render(request,'enroll/userregistraton.html',{'form':fm})
