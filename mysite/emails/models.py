from django.db import models

# Create your models here.
class React(models.model):
    email = models.CharField(max_length=100)
