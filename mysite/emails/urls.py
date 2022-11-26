from django.urls import path
from . import views
from .webscraping import getNewsletter
from .webscraping import sendNewsletter
  
urlpatterns = [
    path('', views.index, name='index'),
    path('getNewsletter', getNewsletter.get_newsletter, name='getNewsletter'),
    path('sendNewsletter', sendNewsletter.send_newsletter, name='sendNewsletter'),
]