from celery import shared_task
from .models import Notifications
from django.contrib.auth import get_user_model
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