from django.shortcuts import render

# Create your views here.
# def show_details(request, my_id):
#     student = {'id':my_id}
#     return render(request,'enroll/show.html',student)

def home_details(request,check):
    print(check)
    return render(request,'enroll/home.html')

def show_details(request, my_id=1):
    if my_id==1:
        student = {'id':my_id, 'name': 'sjkd'}
    if my_id==2:
        student = {'id':my_id, 'name': 'avfd'}
    if my_id==3:
        student = {'id':my_id, 'name': 'jdfvds'}
    return render(request,'enroll/show.html',student)

def show_subdetails(request, my_id=1, my_subid=5):
    if my_id==1 and my_subid==5:
        student = {'id':my_id, 'name': 'sjkd', 'info':'hello1'}
    if my_id==2 and my_subid==6:
        student = {'id':my_id, 'name': 'avfd', 'info':'hello2'}
    if my_id==3 and my_subid==7:
        student = {'id':my_id, 'name': 'jdfvds', 'info':'hello3'}
    return render(request,'enroll/show.html',student)