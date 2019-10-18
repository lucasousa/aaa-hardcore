from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from aaa.models import AAA 

class Director(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    office = models.CharField('Cargo',max_length=255, blank=False, null=False)
    athletic = models.ForeignKey(AAA, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

    def __str__(self):
        return self.user.profile.full_name
    