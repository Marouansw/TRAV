# Generated by Django 4.2.7 on 2024-01-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_flight_type_package_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
