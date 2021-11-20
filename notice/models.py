from django.db import models
from django.dispatch import receiver
from aaa.models import AAA
from django.urls import reverse
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from .utils import gerador_slug_unica
from django.db.models.signals import pre_save
import copy

CROP_SETTINGS = {'size': (395, 191), 'crop': 'smart'}
class Notice(models.Model):
    title = models.CharField(blank=False, max_length=200)
    athletic = models.ForeignKey(AAA, on_delete=models.CASCADE)
    featured_image = ThumbnailerImageField('Imagem de destaque', resize_source=CROP_SETTINGS)
    text = models.TextField(blank=False)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(default='', editable=False, max_length=100)
    is_public = models.BooleanField(verbose_name="Publicada", default=True)
    
    def __str__(self):
        return self.title

    def clone(self, idx):
        cp = Notice.objects.get(pk=idx).copy()
        cp.pk = None
        cp.title = "Cópia:" + cp.title
        cp.is_public = False
        cp.save()

    def copy(self):
        return copy.copy(self)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['published_date']


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = gerador_slug_unica(instance, instance.title, instance.slug) 

pre_save.connect(slug_save, sender=Notice)
