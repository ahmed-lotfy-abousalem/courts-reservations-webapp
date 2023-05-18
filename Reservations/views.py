from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Reservations(request):
 return render(request,'Reservations/reservations.html')