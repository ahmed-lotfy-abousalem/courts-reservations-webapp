from django.urls import path
from . import views

urlpatterns = [
    path('',views.Contact_Us, name="ContactUs" ),
]