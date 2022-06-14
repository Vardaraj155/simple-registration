from django.contrib import admin
from django.urls import path
from student.views import *
from django.contrib.auth import views

urlpatterns = [
    path('',index, name='index'),
    path('logout', logout_view, name='logout'),
    path('register/', registration_view, name='register')
]
