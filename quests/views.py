from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import que



def home(request):
    allhome = que.objects.all()
    return render(request, 'home.html', {'allhome': allhome})     # allhome is var

def base(request):
    return render(request, 'base.html')

def about(request):
     return render(request, 'about.html')

def question(request):
      return render(request, 'question.html')

def login(request):
   return render(request, 'login.html')

def signup(request):
      return render(request, 'signup.html')

def aa(request):
    return render(request, 'aa.html')     

def js(request):
    return render(request, 'js.html')   