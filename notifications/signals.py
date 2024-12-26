from django.db.models.signals import post_save
from .models import Notifications
from django.dispatch import receiver
from order.models import Order
from .tasks import create_notification


@receiver(post_save, sender=Order)
def create_order_notification(sender, instance, created, **kwargs):
    if created:
        create_notification.delay(instance, 'Order Created', 'Your order has been created successfully')
    elif instance.status == 'Pending':
        create_notification.delay(instance, 'Order Pending', 'Your order is pending')
    elif instance.status == 'Shipped':
        create_notification.delay(instance, 'Order Shipped', 'Your order has been shipped')
    elif instance.status == 'Delayed':
        create_notification.delay(instance, 'Order Delayed', 'Your order has been delayed')
    elif instance.status == 'Delivered':
        create_notification.delay(instance, 'Order Delivered', 'Your order has been delivered')
    elif instance.status == 'Cancelled':
        create_notification.delay(instance, 'Order Cancelled', 'Your order has been cancelled')
        

