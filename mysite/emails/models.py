from django.db import models
from django.shortcuts import render

# Create your models here.
class React(models.model):
    email = models.CharField(max_length=100)

# retrieve the email from the database and send it to frontend react app
# def display_email(request):
#     email = React.objects.all()
#     return render(request, 'index.html', {'email': email})

