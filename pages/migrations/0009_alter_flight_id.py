# Generated by Django 4.2.7 on 2024-01-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_flight_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
