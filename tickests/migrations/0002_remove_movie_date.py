# Generated by Django 5.0 on 2023-12-12 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
    ]