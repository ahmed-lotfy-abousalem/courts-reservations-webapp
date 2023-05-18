from django.shortcuts import render
from django.http import HttpResponse

def Contact_Us(request):
    
    return render(request,'Contact_Us/contactus.html')
# Create your views here.
