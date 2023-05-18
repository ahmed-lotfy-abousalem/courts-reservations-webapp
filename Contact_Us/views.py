from django.shortcuts import render
from django.http import HttpResponse

def Contact_Us(request):
    
    if request.method =="POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        message = request.POST['message']
        return render (request,'Contact_Us/contactus.html', {'fullname' : fullname } )
        
    else:
      return render(request,'Contact_Us/contactus.html')
# Create your views here.
