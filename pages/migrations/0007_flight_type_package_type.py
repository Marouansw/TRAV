# Generated by Django 4.2.7 on 2024-01-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_package_checked_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='type',
            field=models.CharField(blank=True, default='FLIGHT', max_length=10),
        ),
        migrations.AddField(
            model_name='package',
            name='type',
            field=models.CharField(blank=True, default='PACKAGE', max_length=10),
        ),
    ]