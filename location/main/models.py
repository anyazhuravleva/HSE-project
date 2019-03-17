from django.db import models
from django.contrib.auth.models import User


class RequestTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
    antenna = models.CharField(max_length=20)     # models.ForeignKey
    date = models.DateTimeField(auto_now=True)


class AntennasTable(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
