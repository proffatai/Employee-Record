"""
URL configuration for Employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"), # if the / path is reached, it calls view.home as well
    path('message/',views.message,name="employee_list"), # if the message/ path is reached, it calls view.message as well 
    path('message/employees/',include('EmployeeApp.urls')) # if the message/employees path is reached, it calls the urls.py in EmployeeApp
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#/message path is executing on the project level, not on the EmployeeApp level. But in the django, we say message/
#/message/employees path is executing on the EmployeeApp level, not on the project level
#/message/employees/1 path is executing on the EmployeeApp level, not on the project level