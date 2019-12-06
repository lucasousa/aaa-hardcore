from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from datetime import date
from django.db import models
from django.utils import timezone
from association.models import Association

# Create your models here.
class Profile(models.Model):
    SEX_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField('Nome completo', max_length=255, blank=False, null=False, default='Anônimo')
    course_name = models.CharField('Nome do curso', max_length=255, blank=False, null=False, default='')
    cpf = models.CharField('CPF', max_length=14, blank=False, null=False, default='')
    date_birth = models.DateField('Data de nascimento', blank=False, null=False, default=timezone.now)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES, blank=False, null=False, default='M')

    @property
    def has_associated(self):
        if Association.objects.filter(user=self.user).exists():
            association = Association.objects.get(user=self.user)
            if association.expired:
                return False
            return True
        else:
            return False

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