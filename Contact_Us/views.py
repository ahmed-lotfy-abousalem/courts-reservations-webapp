from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
from django.contrib import messages

def Contact_Us(request):
    
    if request.method =="POST":
        cntact = contact()
        fullname = request.POST['fullname']
        email = request.POST['email']
        message = request.POST['message']
        
        cntact.fullname = fullname
        cntact.email = email
        cntact.message = message
        
        cntact.save()
        messages.success(request,"Your Message Has Been sent")
        return render (request,'Contact_Us/contactus.html' )
        
    else:
      return render(request,'Contact_Us/contactus.html')
# Create your views here.
