from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
class Mail:
    def __init__(self, email, content, html=False):
        self.email = email
        self.content = content
        self.html = html

    def subscription_send_email(self):
        subject = 'Thank you for subscribing to our daily newsletter!'
        message = self.content
        email_from = settings.EMAIL_HOST_USER
        print(email_from)
        recipient_list = [self.email,]
        if self.html:
            msg = EmailMultiAlternatives(subject, message, email_from, recipient_list)
            msg.attach_alternative(message, "text/html")
            msg.send()
        else:
            send_mail(subject, message, email_from, recipient_list)
        print("Mail sent!")



