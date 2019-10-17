from django.db import models
from aaa.models import AAA 

# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=50,blank = True, null = True)
    logo = models.ImageField(blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    athletic = models.ForeignKey(AAA,blank = True, null = True , on_delete = models.CASCADE)

    def __str__(self):
        return self.name


