# Generated by Django 3.1 on 2020-08-26 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='datetime',
            new_name='date',
        ),
    ]
