from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Otp
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Otp)
def otp_handler(sender, instance, **kwargs):
    print('-------------------')
    send_mail(subject='otp',
              message=f'otp -> {instance.otp}',
              from_email= settings.EMAIL_HOST_USER,
              recipient_list=[instance.email]
              )
