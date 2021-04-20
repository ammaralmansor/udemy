from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from . import form as f
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

def third(request):
    name = "ammar "
    material = ["c++" , "java" , "python"]
    num1 , num2 = 3 , 5
    ans = num1>num2
    mydict = {
        "name" : name,
        "material" : material,
        "ans" : ans
          }
    return render(request,'third.html',context=mydict)


def imagepage(request):
    return render(request,'imagepage.html')

def imagepage2(request,logo):
    logo = str(logo).lower()
    mydict ={"logo": logo}
    return render(request,'imagepage2.html',context=mydict)

def passcolor(request,color):
    color = str(color).lower()
    mydict = {
        "color": color
    }
    return render(request,'passcolor.html',context=mydict)

def form(request):
    return render(request,'form.html')

def submit(request):
    mysubmit={
        "t1": request.GET.get('t1'),
        "t2": request.GET.get('t2'),
        "method" : request.method
        }
    return JsonResponse(mysubmit)

def form2(request):
    mform = f.Feedback(request.POST)
    if mform.is_valid():
        title = request.POST['title']
        subject = request.POST['subject']
        myd ={
            "form":f.Feedback(),
            "valid":True
        }
        print("if")
        if title != title.upper():
            myd['bg']='warning'
            myd['success']=False
            myd['msg']='failer in submitted'
            print("if if ")
            return render(request,'form2.html',context=myd)

        else:
            myd['bg']='success'
            myd['success']=True
            myd['msg']='Form Submiited'
            myd["valid"]=True
            print("if else")
            return render(request,'form2.html',context=myd)

    else:
        mform = f.Feedback(request.POST)
        myd ={
                "form":f.Feedback(),
            }
        myd["valid"]=False    

        print("else")
        return render(request,'form2.html',context=myd)

        