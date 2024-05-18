from django.db import models

# Create your models here.


class Otp(models.Model):
    email = models.CharField(max_length=30)
    otp = models.CharField(max_length=30)
