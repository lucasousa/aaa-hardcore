# Generated by Django 2.2.6 on 2019-10-24 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0009_merge_20191024_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='athletic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaa.AAA'),
        ),
    ]
