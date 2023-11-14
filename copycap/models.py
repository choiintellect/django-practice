from django.db import models

# Create your models here.
class UserRealInput(models.Model):
    text = models.CharField(max_length= 255, null= True)

class InputG2pk(models.Model):
    text = models.CharField(max_length= 255, null= True)