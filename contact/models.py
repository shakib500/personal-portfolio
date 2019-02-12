from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    message = models.TextField()
