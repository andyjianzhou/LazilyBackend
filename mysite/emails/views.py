from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from . import mail as m
from .webscraping import sendNewsletter
from .database import database
from datetime import datetime, timezone
import asyncio
import threading

db = database.MyDatabase('emails.db')
@csrf_exempt

# run the newsletter function every day at 8:00am asynchronously
async def initiate_newsletter(db):
    # print("running")
    Mail = m.Mail
    time = datetime.now(timezone.utc)
    #convert time to local time
    time = time.astimezone()
    hour, minute = time.hour-4, time.minute
    print(hour, minute)
    #send the news letter every day at 8:00am
    if hour == 13 and minute == 2:
            print("=================Newsletter test====================")
    if time.hour == 8:
        #send the newsletter
        print("Sending newsletter")
        content = sendNewsletter.send_newsletter()
        emails = db.fetch()
        for email in emails:
            mail = Mail(email, content, html=True)
            mail.subscription_send_email()
    return HttpResponse("Newsletter sent")
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
            return HttpResponse("Email already exists")
        else:
            db.insert(email)
            #change to html later
            mail = Mail(email, content, html=False)
            mail.subscription_send_email()
            return HttpResponse("Email added")
    return HttpResponse("RUNNING") 

#run the newsletter function every day at 8:00am asynchronously never ending
def newsletter_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(initiate_newsletter(db))
    # loop.run_forever()

# newsletter_thread()

