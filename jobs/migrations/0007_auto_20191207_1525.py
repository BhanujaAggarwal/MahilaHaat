# Generated by Django 2.0 on 2019-12-07 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_applyjob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applyjob',
            old_name='file',
            new_name='CV',
        ),
    ]
