from django.shortcuts import render

# Create your views here.
def learn_django(request):

    #third way
    cname='Django'
    duration='4 months'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats}
    return render(request,'courses/course1.html',context=django_details)
    
    
    # first way 
    # coursename={'cname':'Django'}
    # return render(request,'courses/course1.html',context=coursename)

    # third way
    # return render(request,'courses/course1.html',{'cname':'Django'})

def learn_python(request):
    return render(request,'courses/course2.html')
