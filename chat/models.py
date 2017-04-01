from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.CharField(max_length=200)
    receiver = models.ForeignKey(User, null=True, related_name="reciever")
    sender = models.ForeignKey(User, null=True, related_name="sender")
    time = models.DateTimeField(auto_now=True, null=True)
