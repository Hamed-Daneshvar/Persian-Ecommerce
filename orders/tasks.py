from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@shared_task
def order_created(order_id):
	"""
	Task to send an e-mail notification when an order is
	successfully created.
	"""
	order = Order.objects.get(id=order_id)

	# mail config
	subject = f"Order nr. {order.id}"
	message = f"Dear {order.full_name},\n\n" \
              f"You have successfully placed an order." \
              f"Your order ID is {order.id}."
	mail_sent = send_mail(subject,
						  message,
						  settings.DEFAULT_FROM_EMAIL,
						  [order.email])

	return mail_sent