from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import date
from django.db import models

# Create your models here.
class Profile(models.Model):
    SEX_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    date_birth = models.DateField(blank=False, null=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)

    @property
    def age(self):
        now = date.today()
        return now.year - self.date_birth.year - ((now.month, now.day) < (self.date_birth.month, self.date_birth.day))


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()