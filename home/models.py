from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    email= models.CharField(max_length=122)
    desc= models.TextField(null=True)
    date= models.DateField(auto_now_add=True)
