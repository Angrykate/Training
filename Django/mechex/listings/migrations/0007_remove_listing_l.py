# Generated by Django 5.1.3 on 2024-12-01 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_listing_l'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='l',
        ),
    ]
