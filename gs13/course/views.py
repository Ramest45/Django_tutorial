from django.shortcuts import render
# from datetime import datetime

# Create your views here.
# def learn_django(request):
#     d=datetime.now()
#     return render(request,'course/course1.html',{'dt':d})

# def learn_django(request):
#     return render(request,'course/course1.html',{'p1':56.23143, 'p2':56.0000, 'p3':56.36000})


# def learn_django(request):
#     student={'names':['Sonam','Laxman','Aman','Upendra','Abhinav']}
#     return render(request,'course/course1.html',student)

def learn_django(request):
    data={'stu1':{'name':'Sonam','roll':59},
         'stu2':{'name':'Laxman','roll':32},
         'stu3':{'name':'Upendra','roll':60},
         'stu4':{'name':'Abhinav','roll':23},
        }
    return render(request,'course/course1.html',{'data':data})