import datetime
from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # status = models.Choices()
    date_ordered = models.DateTimeField(default=datetime.datetime.now)
