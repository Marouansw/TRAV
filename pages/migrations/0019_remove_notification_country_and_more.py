# Generated by Django 4.2.7 on 2024-02-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='country',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='depart',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='destination',
        ),
        migrations.AddField(
            model_name='notification',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='notification',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
