from django.db import models
from django.dispatch import receiver
from aaa.models import AAA



class Product(models.Model):
    name = models.CharField(blank=False, null= False, max_length=100)
    description = models.TextField(blank=False, null= False, max_length=200)
    value = models.DecimalField(decimal_places= 2, max_digits= 8)
    value_partner = models.DecimalField(decimal_places= 2, max_digits= 8)

    image = models.ImageField(blank = False, null = False)
    athletic =  models.ForeignKey(AAA, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']
    
    def __str__(self):
        return self.name
            

