Create a new folder where you want to save your project
Create a virtual env: `python3 -m venv nameOfenv`
Activate the virtual env: navigate to the root folder of the main folder/project you created and run the command: `source envName/bin/activate` = `source DjangoProject/bin/activate`
Now cd into the venv: `cd envName`
Then install django: `pip install django` inside the venv
Now proceed to create a django project: `django-admin startproject projectName`
cd into the projectName and then create an app: cd projectName, then `python manage.py startapp appName`


## Some important commands
`python manage.py runserver` for running development server. Run the command inside the Django project
`python manage.py startapp app` for creating a new app in a project
`python manage.py createsuperuser`: for creating superuser
`python manage.py changepassword urUsername`
`python manage.py makemigrations`



   
## Django File Structure
 __init__.py
 wsgi.py : It stands for web server gateway interface. It is used for deploying our application on production servers
 asgi.py: It stands for assynchronous server gateway interface. It is similar to wsgi.py
 urls.py: It contains all the endpoints that our application will be having.
 settings.py: It is used for doing settings and adding other functionality

 ### Django settings.py Explained
 BASE_DIR = Path(__file__).resolve().parent.parent, BASE_DIR is used to get the root directory of the project dynamically
 SECRET_KEY: Secret keys are used to generate hash. Where hashing is the process of encrypting certain data so that it cannot be readable by others. Django generated a random secret key and stored it into a SECRET_KEY variable

 DEBUG=true: THis is set to true by default on the development server. Meaning, as a developer, you'd want to be able to debug the project as you actively develop. But for production server, DEBUG should be set to false so that we dont show any urls or info to the users on prod

 ALLOWED_HOST = []: Here we have to enter the domain name of our website where we want to run the project. We can leave it blank on the dev server and we wont get any errors BUT we must provide the domain name / server ip address of our website when we ship it to prod else there would an error

INSTALLED_APPS=[] : What is an app? An app is a package with django modules. These modules are used to perform business logics. Note: A django project can have multiple apps, with these multiple apps, we can create reuseable components based on the kind of logic we are writing. Whenever we create an app in a django project, we register the name of the app inside the INSTALLED_APPS list

MIDDLEWARE: It is used to perform various functions like security , authentication etc. Django has provided some middlewares for us 

ROOT_URLCONF: This tells us where the main url configuration lies. In this project, the settings.py has it that `ROOT_URLCONF = 'Employee.urls' ` . This implies that the urls can be configured from the Employee folder/urls.py

TEMPLATES: This section is responsible for rendering the frontend templates

WSGI_APPLICATION: This tells django the location where wsgi applications should run from

DATABASES: Where we provide the database we wanna use

AUTH_PASSWORD_VALIDATORS: It helps to check with the strength of password entered by the user. It is comes with django by default

LANGUAGE_CODE: we can set the language code of our project. Default is English-US

TIME_ZONE = 'UTC': we can change the timezone of the project

USE_I18N = True: This means that we wanna use internationalization in our project.(Internationalization is talking about us being able to make our project appear in different language when set to True)

USE_TZ = True : This means use timezone

STATIC_URL: The CSS and JS we use in a website/webapp in a Django project are called static files. In Django, we have to do a special configurations for running static files

## How Django works

It uses MVT: Model View Template design pattern

Model: It is responsible for each and every database operations. If we wanna do anything related to DB, we must contact Model
Template: This houses whatever that can be seen by the user. It is known as the frontend layout. Whatever we want to show to the user should be placed inside the template
View: This acts as the link between the template and the model.  View is usually a function where we write the logic. Since view cannot directly interact with the DB, we need models. View speaks to Models to get data and it passes the data to template to display on the frontend

### Practical example
Let's say a user wants to visit our django website to see his username and password which are obviously stored on the DB. He access the django web app via a url (in django we store all the urls that can be used to access our application in a file called urls.py using the inbuilt function called path, `path('nameOfpath/', views.functionThatHousesTheImplementation)` e.g path('about/', views.about) ) where about is a function inside the views.py file[VIEW]

So when a request comes in, e.g we wanna visit facebook.com which is implicitly the same as facebook.com/index. the path goes to the project level urls where we have the urlPattern listed to see if the url / endpoint that we wanna access exists or not. 
If url exists, then the app will now launch the corresponding view (function) that we have for that endpoint(index), so views.index will be called. Now the index function will send a request to models to help fetch the credentials that was requested for from the DB.

Now when going back, if the request (credentials) exist in the DB,it is gotten and stored on models which is then pushed to views and then finally to template(client)

## Starting something
run `python manage.py runserver` to start the server. Assuming we wanna visit a path e.g home from the default url. http://127.0.0.1:8000/home.

We need to go to the urls.py file of the django project and register that path under the urlPatterns list. say `path ('home/', views.home)`. Always end the endpoint/path with `/, ie home/`.  Then we have to call the view to execute once the path is hit. which is views.home.
NB we can also have `path('', views.home)` meaning when the base url is hit without any path, the home page should be called.

In otherwords, we need to create a module/file called views and also create the function home inside views file.
Create a file called views.py inside the project Employee , create a function home and write whatever the action inside the function and then import that file inside urls.py

Our views has the home function below

from django.http import HttpResponse
def home(request): #the function must take in request as a parameter
    return HttpResponse("Hello") #here the function is returning an http response that we must import from django.http module

### Rendering real html or a page that has html, css and js to the user
create a folder that holds our templates files inside the root folder of the django project named e.g`myTemplates`. In otherwords, the template folder should be at the same level as the manage.py file which is inside the project
Create your html files `e.g index.html` inside the templates folders


Note: we have to do some configurations inside the settings file. We need to navigate to the TEMPLATES section then under DIRS and enter the name of the folder we created as in `'DIRS': [ 'myTemplates']`.  By doing this, we have stored the myTemplates inside our django app and then we can access the files inside the myTemplates folder directly since the root folder `myTemplates` has been stored

Our views file can now be

def message(request):
    return render(request, 'index.html') : we will use the render function to render an html file on the web and the function takes in 2 params: request and the name of the file you wanna render. 
    Note: we could pass the name of the html file directly into the render function because we have registered the directory into DIRS that takes note of any directory created in the project[root of the project]
PS: we need to import the render function using, `from django.shortcuts import render`

## Working with css, js and assets files like images or videos
link the css file we created to the html file, i.e inside the html file, include this on the head tag: `<link rel="stylesheet", href="css/style.css">`

In Django we need to create a folder called static inside the inner folder of the actualç project, then inside this folder, we can pass our css, js or other assets into it. Recall that inside the settings file, under `STATIC_URL='static/'`has been set already so this new folder that we just created has been tracked by django by default in as much as we set the name of the file to be stati, else we have to pass the name of the folder we created to the STATIC_URL variable.

Next is to create 2 new variables inside the settings.py, beneath the STATIC_URL variable:
At the top of the settings file add `import os.path` to it
1. `STATIC_ROOT=os.path.join(BASE_DIR,'static')`  <= pass it this way to provide the root where the static files should be taken from
2. `STATICFILES_DIRS=[os.path.join(BASE_DIR,'Employee/static')]` ; STATICFILES_DIRS takes a list of the location where all the static files is. `location to the static file as a string` 

Now, after setting the settings file, we need to go to the html page where we are loading the static files and then include the line 
`{%load static%}` on the very first line of that html file
secondly, we have to update wherever we have used the static file e.g: Recall we imported the css file simply as `<link rel="stylesheet", href="css/style.css">` BUT since our app cant detect the CSS file this way, we have to update it to `<link rel="stylesheet", href="{% static 'css/style.css' %}">`. This way, the css file will be implemented 



## DJANGO APPs
We can have multiple apps inside one django project. Say for example we are building an e-commerce app, we can create different apps to handle different features like users, products, orders, etc. 

### Django Apps project level structure
After creating an app via: `django-admin startproject projectName` we have the following files created:
1. init.py : This tells the interpreter that the director is not a mere folder but a django package
2. admin.py : this is used to configure our admin panel. Run the server and visit the /admin path to access the admin panel. We must have ran the `python manage.py migrate` command before we can access the admin panel
3. apps.py : This file is used to configure the app
4. models.py: This file is used to store essential fields and behaviour of the data that we are storing in the DB. We create DB tables and field by writing some codes into this file
5. tests.py : used to run tests
6. views.py : used to write business logic for a specific app

1. NB: Django provides users with some default database tables to manage the admin panels and other django related stuffs, we need to run the command `python manage.py migrate` to ensure the default DB tables get created in the DB
2. After creating an app, we have to register it in the settings.py file. We need to add the app name to the INSTALLED_APPS variable. In this case, our app name is EmployeeApp and we have to add it to the INSTALLED_APPS variable as below: `INSTALLED_APPS = [ 'EmployeeApp',]`. This is a list of all the apps that we want to use in our project.
3. After registering the app, we need to add the app name to the urls.py file. We need to add the app name to the urlpatterns variable. In this case, our app name is EmployeeApp and we have to add it to the urlpatterns variable as below: `url

   ## Creating models inside models.py
We can store some data into a DB and we can also fetch those data. Django comes with sqlite3 DB. For now we can use the default DB provided by django which is the sqlite3 (Go to the project and go to settings, you'd find the default DB there).

Our task now is to create tables/models for the data we want to store. By default we can use the default database configuration inside the settings.py file. To create tables and fields, we will do that inside models.py as seen below

We want to create a model for storing employee data, in doing so, we will need some fields like firstname, lastname, email and photo etc.
# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length = 100)
    lastname=models.CharField(max_length = 100)
    email=models.EmailField(max_length = 10, unique=True)
    designation=models.CharField(max_length = 100)
    phonenumber=models.CharField(max_length = 11)
    photo=models.ImageField(upload_to= "images") #to use imagefield, we have to install pillow in our environment,using `python -m pip install Pillow`
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)

After creating this model, we have to migrate it (meaning, we have to  create them as a tables in the database). To do that, we run the command `python manage.py makemigrations` and then `python manage.py migrate`

Running `python manage.py makemigrations` will read our models.py and create a migration file for us. This file will contain all the changes that we have made to our models.py file. To identify it, we will go to our app and then inside the migraytions folder, we will see 00001.py file that has the configuration we created for our model.  

Running `python manage.py migrate` will execute the SQL command and create the tables that we need in our DB. To view it, we can check the admin panel to view it.

Note: before we can view the tables on the admin panel, we have to register the model inside the admin.py file of the app by adding the line `admin.site.register(employees)`. Now we can runserver to view the tables on the admin panel

Note that on django admin panel, the name of the table has a default s attached to it. So if the model name is employees, i.e the class name inside the models.py is employees, the table on django admin would be employeess with an additional s.

## Media files
In django, any files that are uploaded by the users are called media files. We need to handle these media files specially so we can have access to it. ` photo=models.ImageField(upload_to= "images")` this line creates a folder `images` on the root directory of the project, similar to the template folder and it holds any images user uploads .
In other to load the media files in our project, we need to create a folder in the root directory of the app named `media` then we need to go to the bottom of settings.py file and set the following lines:

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

In doing this, when we upload any file, this file will be stored inside the media directory and not the root folder anymore. Before this can work, we need to append the following line to the urlspattern variable inside the urls.py file: +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT). And then import settings and static at the top of the file

By doing all these, we can now upload files into the web app and we will be able to view it.

## Using the backend data on the frontend
First thing is to go the templates folder and create a folder named `employees` inside it. Then inside this folder, we will create a file named `index.html` and inside this file, we will write the code to display the data that we have stored in the DB as follows. open the views.py file of the project that has the function to be called when the user visits a certain page. In this case, locate the message() since that is where we want to display the records coming from the DB/Backend.

When we want to fetch data from a model, we first go inside the model then .objects to get each of the object and a query of our choice e.g    `employees.objects.all()` meaning we want all the objects from the emloyees object. PS: we must import this file inside the views.py file  

Inside views.py file where we wrote the command to be called when the path /message is visited
def message(request):
    emp = employees.objects.all() 
    context = {'employee':emp} # This holds the all the objects as a key value pair stored in a variable context. Also, emp is stored inside employee variable and we can use employee inside the index.html file
    return render(request, 'index.html', context)

### Printing python variable inside html file

{% for e in employee %}# to print out a block of code
actions are here
{% endfor %}  #we have to close the for loop
{% %} this is called template tag.It tells the interpreter that here comes something other than a plain html
{{variableName}} #double curly braces to print variable. It is called template variable
e.g {{employee}} #this will print all the values of emp.  

We can just wrap this line of code inside the html file where we want to use the data without importing anything:
{% for i in employee%}
{{i}} #to print all the objects 
{{i.fieldname}} # to display a specific field whether firstname or lastname etc
{% endfor %} 

NB: to print dynamic numbers that can be used as id, we can use JS default for loop counter by writing `forloop.counter`

Finally, we can go to the admin panel to add more data and we can also remove any one of our choice.

## To build the employee details page so that it appears when user clicks on the fullname of the employee

To build a new feature, we have to envision the kind of url pattern that will be needed. Here we want to see the details of each employee, so we should have a path like /employee/id, where id is the id of the employee that will be clicked, by so doing, we can pass the id as a parameter to the function that will be called when the user clicks on the name of the employee.

Now we need to proceed to the project urls.py since all the requests initially comes to this file. We now add a path `employee/` to the urlspattern variable as     `path('employee/',include('EmployeeApp.urls'))`,Meaning   if the /employee path is reached, it calls the urls.py in EmployeeApp.
PS: we need to create urls.py inside the app and we have to import include from django.urls into the file. We must use include() if we want to forward the request into an app that we created in the project. But if the path that we wanna route to is in the project already, we just need to write the path in the urlspattern variable.

Now inside urls.py file of the app, we will import path and include the code

```urlpatterns = [
path('<int:id>/', views.employee_detail), #when any integer is passed as the path to the url, employee_detail function is called with the id as the argument
]```

where <int:id>, is stating that we are expecting a random integer number that we could be1,2,3,etc, so we used id to denote it. If we wrote only id, it means we are expecting a string value. Now when the id path is reached, we call the function employee_details from views of EmployeeApp

For the view.py inside the EmployeeApp, we can create the employee_details () as below and also import these modules:

from django.shortcuts import get_object_or_404, render
from .models import employees
def employee_detail(request, id,context): # asides taking request as a parameter, we have to pass id since we are expecting it to be able to identify each employee
    emp=get_object_or_404(employees, pk=id) # we have to pass the class name [the class where the model were created] and pk=id, pk is the primary key of the object. pk is a unique identifier of each object. We just need to pass something else which i called id
     #we are getting the object one at a time OR 404 means when the object does not exist, it throws a 404 error
    return render(request, 'employee_detail.html', context) # Now we are displaying the employee_detail.html file when the path is reached. We need to create an employee_detail.html file inside the templates folder of the app.
  
  ## We want to render the employee page by creating employee_detail.html file

  We have to create employee_detail.html file inside the templates folder.  We can design the page to display a card and we can use the bootstrap card by searching `bootstrap card` that has image on google and then pasting the code from bootstrap into our code

From the bootstrap we got, we did some modifications, by browing how to centralize the div

    <div class="card mx-auto" style="width: 18rem; margin: 0 auto;">
        <h3>{{employee}} Details</h3> #here we displayed the employee's fullname as the title. We could have used `<h3>{{employee.firstname}} {{employee.lastname}} Details</h3>`
        <img class="card-img-top" src="{{employee.photo.url}}" alt="Card image cap"> # to get the image, we need to call the object and then acces the photo but since image is stored in the database, we need to call the photo.url to get the image.
        <div class="card-body">
          <h5 class="card-title">{{employee.fullname}}</h5>
          <p class="card-text">{{employee.designation}}</p>
          <p class="card-text">{{employee.email}}</p>
          <p class="card-text">{{employee.phonenumber}}</p>
          <a href="{% url 'employee_list'%} " class="btn btn-primary">Go Back</a>
        </div>
      </div>

For the back button, we can browse how to implement it and put it in the code as follows:
We passed, `{% url 'employee_list'%}` as the href attribute of the button. We have to pass the url of the page that we want to go back to. We can use the url of the page that we want to go back to by using the `{% url 'employee_list'%}` since we have given a name=employee_list in the project urlspattern for the employees path

## Adding feature to enable user click the name of the employee and then opens the employees details page.

Firstly, we need to name the employee details page inside the app urls.py, I named it profiles so that I can easily redirect to it as seen below
`path('<int:id>/', views.employee_detail, name="profile")`

Now inside the index.html file, we need to wrap the names of the employee inside an anchor tag and for the href, we have to pass a url to the employee_detail page which has been dubbed as profile, as well as the id of that employee. As seen below
  `<td><a href="{% url 'profile' i.id%}">{{i.firstname}}  {{i.lastname}}</td></a>`


id is an implicit attribute that the object of the class has
