# Generated by Django 2.2.5 on 2019-10-27 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neigh1', '0019_bussines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bussines',
            old_name='user',
            new_name='profile',
        ),
    ]