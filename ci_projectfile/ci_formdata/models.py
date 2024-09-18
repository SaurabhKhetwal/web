from django.db import models

# Create your models here.
class form(models.Model):
    form_fullname=models.CharField(max_length=30)
    form_email=models.CharField(max_length=30)
    form_number=models.CharField(max_length=50)
    form_choice=models.TextField()