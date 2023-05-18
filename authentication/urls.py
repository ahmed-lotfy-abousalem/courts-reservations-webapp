from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.main, name="main"),
    path('signin',views.signin, name="signin"),
    path('signup',views.signup, name="signup"),
    path('signout',views.signout, name="signout"),
]