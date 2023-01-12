from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
