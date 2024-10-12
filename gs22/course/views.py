from django.shortcuts import render

# Create your views here.
def django_learn(request):
    return render(request,'course/courseinfo.html')
