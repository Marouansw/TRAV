# Generated by Django 4.2.7 on 2024-02-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_notification_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
