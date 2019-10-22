# Generated by Django 2.2.6 on 2019-10-17 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aaa', '0004_auto_20191017_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aaa',
            name='created_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de creação'),
        ),
        migrations.AlterField(
            model_name='aaa',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome da AAA'),
        ),
        migrations.AlterField(
            model_name='aaa',
            name='value_association',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da associação'),
        ),
    ]