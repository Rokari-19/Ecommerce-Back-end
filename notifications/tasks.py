from celery import shared_task
from .models import Notifications
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
# from 

@shared_task
def create_notification(instance, title, message):
    obj = get_user_model()
    user = obj.objects.get(id=instance.user.id)
    Notifications.objects.create(
        user=user,
        title=title,
        message=message,
    )
    
    
@shared_task
def send_email(instance, title, message):
    obj = get_user_model()
    user = obj.objects.get(id=instance.user.id)
    emailmessage = EmailMessage(
        subject=title,
        body=message,
        to=[user.email],
        
    )



'''
todo: setup simplejwt for authentication
'''