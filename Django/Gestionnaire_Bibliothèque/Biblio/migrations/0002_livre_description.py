# Generated by Django 5.1.6 on 2025-03-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
