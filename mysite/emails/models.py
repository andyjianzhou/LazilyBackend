from django.db import models

# Create your models here.
# class React(models.model):
#     email = models.CharField(max_length=100)
class React(models.Model):
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.email
