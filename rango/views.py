from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='/rango/about/'>About</a>\nRango says hey there partner!")

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>\nRango says here is the about page.")