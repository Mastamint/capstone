from django.db import models
from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField

class MyUser(AbstractUser):
    json = JSONField()
    ...