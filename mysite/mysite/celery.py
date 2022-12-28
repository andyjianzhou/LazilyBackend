from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from emails.tasks import send_morning_newsletter
from celery import shared_task
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')
app.conf.enable_utc=False
app.conf.update(timezone='US/Mountain')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send-morning-newsletter': {
        'task': 'send_morning_newsletter',
        # every 8 am
        # 'schedule': crontab(hour=8, minute=0), # every 8 am
        'schedule': 30.0,
        'args': ()
    },
}
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')