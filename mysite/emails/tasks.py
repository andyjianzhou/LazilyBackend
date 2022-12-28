
from .migrations.webscraping import sendNewsletter
from .migrations.database import database
from . import mail as m
# import app from celery file
# from mysite.celery import app
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

@shared_task(name="send_morning_newsletter")
def send_morning_newsletter():
    try:
        Mail = m.Mail
        db = database.MyDatabase('emails.db')
        emails = db.get_all()
        print(emails)
        # send to all emails in the database without using a for loop
        mail = Mail('andyzhou727@gmail.com', sendNewsletter.send_newsletter(), html=True)
        # call the subscription_send_email() method on the instance
        mail.subscription_send_email()
        print("Mail sent succesfully!")
    except Exception as e:
        print('Error:', e)
    return "Function ran successfully!"


# Run command to run celery
# celery -A mysite worker -l info
# celery -A mysite beat -l info
# kill the celery process in windows terminal
# taskkill /F /IM celery.exe
# celery -A mysite worker -l info

# kill theh ceelery beat process in windows terminal
# taskkill /F /IM celerybeat.exe
# how to know if the celery beat is running or not in windows terminal
# netstat -ano | findstr :6379
# To know the process id of the celery beat
# tasklist | findstr celerybeat.exe
# To kill the celery beat process
# taskkill /F /IM celerybeat.exe
# To run the celery beat
# celery -A mysite beat -l info