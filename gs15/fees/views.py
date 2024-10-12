from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request,'fees/fees1.html',{'name':'Djnago','fees':'3000'})
