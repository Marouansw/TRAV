# Generated by Django 4.2.7 on 2024-01-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_flight_hour_a_flight_hour_d_flight_ps1_flight_ps2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='checked_out',
            field=models.CharField(blank=True, default='no', max_length=10),
        ),
    ]
