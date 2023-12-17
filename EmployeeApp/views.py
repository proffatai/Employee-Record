from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import employees
# Create your views here.
def employee_detail(request, id): #recall, from urls.py, when we called the employee_detail(), an id is passed with it so we have to receive it here and use it to call the image of a specific employee
    emp=get_object_or_404(employees, pk=id) 
    context = {'employee':emp} # we want to pass the object to an html file so we have to use the context dictionary format as we did earlier
    return render(
        request, 'employee_detail.html',context)