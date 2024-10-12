from django.shortcuts import render
from . import views

# Create your views here.
def fee_django(request):
    return render(request,'fees/info.html',{'fee':'Django fees'})
