from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from . import form as f
import re
# Create your views here.

def error_404_view(request,exception):
    return render(request,'404.html')

def about(request):
    return HttpResponse("About")


def add(request, a, b):
    return HttpResponse("Resault : {}".format(a+b))


def intro(request, name, age):
    mydict = {
        "name": name,
        "age": age
    }
    return JsonResponse(mydict)


def example(request):
    return render(request, 'example.html')


def index(request):
    return render(request, 'index.html')


def third(request):
    name = "ammar "
    material = ["c++", "java", "python"]
    num1, num2 = 3, 5
    ans = num1 > num2
    mydict = {
        "name": name,
        "material": material,
        "ans": ans
    }
    return render(request, 'third.html', context=mydict)


def imagepage(request):
    return render(request, 'imagepage.html')


def imagepage2(request, logo):
    logo = str(logo).lower()
    mydict = {"logo": logo}
    return render(request, 'imagepage2.html', context=mydict)


def passcolor(request, color):
    color = str(color).lower()
    mydict = {
        "color": color
    }
    return render(request, 'passcolor.html', context=mydict)


def form(request):
    return render(request, 'form.html')


def submit(request):
    mysubmit = {
        "t1": request.GET.get('t1'),
        "t2": request.GET.get('t2'),
        "method": request.method
    }
    return JsonResponse(mysubmit)


def form2(request):
    mform = f.Feedback(request.POST)

    if mform.is_valid():

        title = request.POST['title']
        subject = request.POST['subject']
        email = request.POST['email']
        phone = request.POST['phone']
        myd = {
            "form": f.Feedback(),
        }

        errorflag = False
        Error = []

        if title != title.upper():

            errorflag = True
            errormsg = "Title should be in Capital"
            title_tips = "eig: TITLE"
            title_tuple = (errormsg, title_tips)
            Error.append(title_tuple)

        email_patt = "^[a-z][a-zA-Z0-9]+@[a-z]+.com$"

        if not re.search(email_patt, email):

            errorflag = True
            errormsg = "Not a valid Email Address"
            email_tips = "eig: ammar123@gmail.com"
            email_tuple = (errormsg, email_tips)
            Error.append(email_tuple)

        phone_patt = "^00963[0-9]{9}"
        if not re.search(phone_patt, phone):

            errorflag = True
            errormsg = "Not a vslid Phone "
            phone_tips = "eig: 00963987654321"
            phone_tuple = (errormsg, phone_tips)
            Error.append(phone_tuple)

        if errorflag == False:
            myd["success"] = True
            myd["successmsg"] = "Success Submitted"

        myd["error"] = errorflag
        myd["errormsg"] = Error
        return render(request, 'form2.html', context=myd)

    else:
        mform = f.Feedback(request.POST)
        myd = {"form": f.Feedback()}
        return render(request, 'form2.html', context=myd)
