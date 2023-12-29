from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import employees
# Create your views here.
def employee_detail(request, id): #recall, from urls.py, when we called the employee_detail(), a dynamic integer id which serves as the path is to be reached / serves as the specific employee whose details we wanna see, we need to pass d the id of the specific employee that we wanna displays his full info as the path and also use it  to get the specific employee from the objects
    emp=get_object_or_404(employees, pk=id) # here we are getting/extracting the details of a specific employee with id
    context = {'employee':emp} # we want to pass the object to an html file so we have to use the context dictionary format as we did earlier
    return render(
        request, 'employee_detail.html',context)