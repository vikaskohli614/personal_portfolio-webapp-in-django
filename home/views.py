from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')
    #return HttpResponse(' this is services page')
    

def Mycv(request):
    return render(request,'MyCV.html')
    #return HttpResponse(' this is mycv page')

def blog(request):
    return render(request,'Blog.html')
    #return HttpResponse(' this is blog page')


def Contacts(request):
    return render(request,'Contact.html')


def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        object = Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
        object.save()
    return render(request,'Contact.html')
    #return HttpResponse(' this is contact page')    