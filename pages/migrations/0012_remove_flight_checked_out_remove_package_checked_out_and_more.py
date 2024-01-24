# Generated by Django 4.2.7 on 2024-01-19 20:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0011_flight_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='checked_out',
        ),
        migrations.RemoveField(
            model_name='package',
            name='checked_out',
        ),
        migrations.AddField(
            model_name='flight',
            name='checked_out_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='package',
            name='checked_out_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
