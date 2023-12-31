from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.get_username
