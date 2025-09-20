from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Register, name="reg"),
    path('show',views.Showdata, name="show"),
    path('show/delete/<str:id>',views.delete, name="delete"),
]