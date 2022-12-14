from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from . import mail as m
from .migrations.webscraping import sendNewsletter
from .migrations.database import database
from .migrations.webscraping import sendNewsletter


db = database.MyDatabase('emails.db')
@csrf_exempt
def index(request):
    # Get the data sent from the client
    #retrieve request body
    Mail = m.Mail
    db = database.MyDatabase('emails.db')
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['params']['email'] 
        content = f"Hello {email}, thank you for subscribing to our daily newsletter!"
        if db.check(email):
            content = "You are already subscribed to our daily newsletter!"
            mail = Mail(email, content, html=False)
            mail.subscription_send_email()
            # send html page sendNewsletter.get_newsletter()
            # mail = Mail(email, sendNewsletter.send_newsletter(), html=True)
            # mail.subscription_send_email()
            return HttpResponse("Email already exists")
        else:
            db.insert(email)
            #change to html later
            mail = Mail(email, content, html=False)
            mail.subscription_send_email()
            return HttpResponse("Email added")
        
    
    return HttpResponse("RUNNING") 


# create a REST api to send the database information to the frontend
@csrf_exempt
def sendNewstoFrontend(request):
    if request.method == 'GET':
        db = database.MyDatabase('emails.db')
        emails = db.fetch()
        # turn into json
        emails = json.dumps(emails)
        print(emails)
        return HttpResponse(emails)
    return HttpResponse("RUNNING")


