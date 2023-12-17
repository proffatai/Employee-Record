from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length = 100)
    lastname=models.CharField(max_length = 100)
    email=models.EmailField(max_length = 100, unique=True)
    designation=models.CharField(max_length = 100)
    phonenumber=models.CharField(max_length = 11)
    photo=models.ImageField(upload_to= "images") 
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at=models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.firstname +" "+self.lastname #this is done so that we can represent each record with the firstname and last name on the admin panel