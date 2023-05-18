from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ResFoot(request):
 return render(request,'ResFoot/ResFoot.html')