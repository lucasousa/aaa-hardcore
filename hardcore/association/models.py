from django.db import models

# Create your models here.
class Association(models.Model):
    #user = models.ForeignKey()
    date_entry = models.DateField()
    expiration_date = models.DateField()

    @property
    def expired(self):
        pass

