from django.urls import path
from . import views

urlpatterns = [
path('<int:id>/', views.employee_detail), #when any integer is passed as the path to the url, employee_detail function is called with the id as the argument
] #app level url