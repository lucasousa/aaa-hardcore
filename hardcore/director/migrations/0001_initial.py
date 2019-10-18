# Generated by Django 2.2.6 on 2019-10-17 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aaa', '0009_auto_20191017_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=255, verbose_name='Cargo')),
                ('athletic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Diretor',
                'verbose_name_plural': 'Diretores',
                'ordering': ['name'],
            },
        ),
    ]
