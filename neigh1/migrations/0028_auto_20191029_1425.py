# Generated by Django 2.2.6 on 2019-10-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neigh1', '0027_neighborhoodpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhoodpost',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
