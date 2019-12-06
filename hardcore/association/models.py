from django.db import models
from django.contrib.auth.models import User
from aaa.models import AAA 
import datetime

# Create your models here.
class Association(models.Model):
    date_entry = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    athletic = models.ForeignKey(AAA, on_delete = models.CASCADE)

    @property
    def expired(self):
        if datetime.date.today() > self.expiration_date:
            return True
        else:
            return False

    def __str__(self):
        return self.user.profile.full_name

