from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login(request):
    return render(request, 'regLogin/login.html')

def register(request):
    return render(request, 'regLogin/register.html')