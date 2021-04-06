from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
# Create your views here.


def about(request):
    return HttpResponse("About")

def add(request,a,b):
    return HttpResponse("Resault : {}".format(a+b))

def intro(request,name,age):
    mydict = {
        "name" : name ,
        "age"  : age
    }
    return JsonResponse(mydict)

def example(request):
    return render(request,'example.html')
    
def index(request):
    return render(request,'index.html')


