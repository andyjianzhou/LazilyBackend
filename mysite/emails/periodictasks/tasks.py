# task file
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from ..migrations.webscraping import sendNewsletter
import time
import datetime
from django.template.loader import render_to_string
from ..migrations.database import database
from .. import mail as m
from celery.schedules import crontab
from celery import periodic_task

@periodic_task
def send_newsletter():
    db = database.MyDatabase('emails.db')
    mail = m.Mail()
    emails = db.get_all()
    mail.Mail(emails, sendNewsletter.get_newsletter(), html=True)
    mail.subscription_send_email()
    print("Newsletter sent!")

# Run command to run celery
# celery -A mysite worker -l info