# Generated by Django 4.2.7 on 2024-01-20 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_flight_checked_out_remove_package_checked_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]