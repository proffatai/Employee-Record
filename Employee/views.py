from django.http import HttpResponse
from django.shortcuts import render
from EmployeeApp.models import employees

def home(request):
    return HttpResponse("Hello") # we can return an html or we say, render an html file

def message(request):
    emp = employees.objects.all() #this is to return all the objects as a set
    context = {'employee':emp} # this is to map each object with the context
    return render(request, 'index.html', context) # we can return an html or we say, render an html file. We also need to pass the context to the html page

