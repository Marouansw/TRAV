# Generated by Django 4.2.7 on 2024-02-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_package_pack_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='image',
        ),
    ]