from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/Home.html',{'nm':'Django','description':'This is my Home page.'})

def about(request):
    return render(request,'core/about.html',{'name':'Django'})