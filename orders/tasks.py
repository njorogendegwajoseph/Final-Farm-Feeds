from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    '''Task to send email, after user has made an order'''
    order = Order.objects.get(id=order_id)
    subject = f'Order number {order.id}'
    message = f'Dear {order.first_name}, \n\n'\
              f'You have successfully placed an order' \
            f'Your order number is {order.id}'
    message_sent = send_mail(subject, message, 'josephnjorogendegwa@gmail.com', [order.email])
    return message_sent
     