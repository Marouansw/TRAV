# Generated by Django 4.2.7 on 2024-02-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_alter_package_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='pack_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
