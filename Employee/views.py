from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return HttpResponse("Hello") # we can return an html or we say, render an html file

def message(request):
    return render(request, 'index.html')