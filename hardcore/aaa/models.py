from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class AAA(models.Model):
    name = models.CharField('Nome da AAA',max_length=255, blank=False, null=False)
    created_data = models.DateField('Data de criação',blank=False, null=False, default=timezone.now)
    logo = models.ImageField()
    value_association = models.DecimalField('Valor da associação',decimal_places=2, max_digits=8, blank=False, null=False )

    @property
    def qtd_members(self):
        pass

    class Meta:
        verbose_name = 'AAA'
        verbose_name_plural = 'AAAs'
        ordering = ['name']

    def __str__(self):
        return self.name
