from django.shortcuts import render
from . import views

# Create your views here.
def home_django(request):
    return render(request,'Home.html',{'hlw':'Home Page'})

