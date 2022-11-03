from django.db import models

# Create your models here.



class Domain(models.Model):
    domain = models.CharField(max_length=253)
    is_up = models.BooleanField(null= True, blank = True)