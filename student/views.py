from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from student.forms import registration
from student.models import *



# Create your views here.

def index(request):
    context={}
    details=Student.objects.all()
    context['details']=details

    return render(request, 'index.html',context) 


def registration_view(request):
    context={}
    if request.POST:
        formreg =registration(request.POST)
        if formreg.is_valid():
            formreg.save()
            email=formreg.cleaned_data.get('Email')
            username=formreg.cleaned_data.get('username')
            raw_password=formreg.cleaned_data.get('password1')
            account=authenticate(username=username, password=raw_password)
            return redirect('index')
        else:
            context['registration']=formreg
    else:
        formreg=registration()  
        context['registration']=formreg
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')


