from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from ci_formdata.models import form

# Create your views here.

def homepage(request):
    return render(request,"index.html")

def contactus(request):
    return render(request,"contactus.html")
 
def saveEnquiry(request):
    
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=form(form_fullname=name,form_email=email,form_number=phone,form_choice=message)
        
        print(name,email,phone,message,data)
        

        
        data.save()
    # else:
    #     print(form.errors)
        
    return render(request,"contactus.html")

def success(request):
    return render(request, 'success.html')

def Ourservices(request):
    return render(request,"Ourservices.html")

def aboutus(request):
    return render(request,"about-us.html")

def web_development_page(request):
    return render(request,"web-development-page.html")

def ux_ui_page(request):
    return render(request,"ui-ux-page.html")

def app_develpment_page(request):
    return render(request,"app-development.html")

def digitalmarketing(request):
    return render(request,"digitalmarketing.html")


