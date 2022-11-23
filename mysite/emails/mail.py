from django.core.mail import send_mail  
from django.conf import settings

def send_news(email):
    subject = 'Welcome to my site'
    message = f'Hi {email}, thanks for signing up'
    email_from = settings.EMAIL_HOST_USER
    print(email_from)
    recipient_list = [email,]
    
    send_mail(
        subject, 
        message, 
        email_from, 
        recipient_list,
        )
    print("Mail sent!")


