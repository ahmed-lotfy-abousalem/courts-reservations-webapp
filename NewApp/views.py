from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def unique(request):
    
    return render(request,'NewApp/home.html')