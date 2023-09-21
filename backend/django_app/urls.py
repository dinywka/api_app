from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('api/', views.api),
    path('add_complaint/', views.add_complaint),
    path('add_complaint/<str:point_id>', views.add_complaint),
]