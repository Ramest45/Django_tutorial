from django.shortcuts import render
from .forms import Studentregistration, Teacherregistration

# Create your views here.
def Student_data(request):
    if request.method == "POST":
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = Studentregistration()  # Reset the form after saving
    else:
        fm = Studentregistration()
    
    return render(request, "enroll/Student.html", {"form": fm})

def Teacher_data(request):
    if request.method == "POST":
        nm = Teacherregistration(request.POST)
        if nm.is_valid():
            nm.save()
        nm = Teacherregistration()  # Reset the form after saving
    else:
        nm = Teacherregistration()
    
    return render(request, "enroll/Teacher.html", {"form": nm})
