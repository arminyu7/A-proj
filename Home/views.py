from django.shortcuts import render
from .models import Todo

def say_hello(request):
    person = {'name':'admin'}
    return render(request, "hello.html", context=person)

def home(request):
    all = Todo.objects.all()
    return render(request, "home.html", {'todos': all})

