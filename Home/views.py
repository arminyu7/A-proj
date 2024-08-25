from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello user...")

def home_page(request):
    return HttpResponse("welcome to my site")