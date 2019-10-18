from django.db import models
from django.dispatch import receiver
from aaa.models import AAA
from django.urls import reverse


class Notice(models.Model):
    title = models.CharField(blank=False, max_length=200)
    athletic =  models.ForeignKey(AAA, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField('Slug', max_length=100)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['published_date']
    
    def __str__(self):
        return self.title

