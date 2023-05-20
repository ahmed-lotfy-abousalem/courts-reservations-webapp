from django.urls import path
from . import views

urlpatterns = [
    path('',views.SquashRes, name="SquashRes"),
    path('save-date/', views.save_date, name='save_date'),
    path('success/<str:selected_date>/', views.success, name='success'),
]