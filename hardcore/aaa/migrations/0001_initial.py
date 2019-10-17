# Generated by Django 2.2.6 on 2019-10-17 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aaa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('logo', models.CharField(max_length=255)),
                ('value_association', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
