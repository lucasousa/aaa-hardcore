from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Director():
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField('Cargo',max_length=255, blank=False, null=False)
    