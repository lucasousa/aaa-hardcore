from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Aaa(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    created_data = models.DateTimeField(default=timezone.now)
    logo = models.CharField(max_length=255, blank=False, null=False)
    value_association = models.DecimalField(decimal_places=2, max_digits=8)

    def qtd_members(self):
        pass

    def __str__(self):
        return self.name
