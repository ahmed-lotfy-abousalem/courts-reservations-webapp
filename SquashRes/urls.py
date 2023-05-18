from django.urls import path
from . import views

urlpatterns = [
    path('',views.SquashRes, name="SquashRes"),
]