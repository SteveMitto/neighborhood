# Generated by Django 2.2.5 on 2019-10-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neigh1', '0011_auto_20191027_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nation',
            name='calling_codes',
            field=models.CharField(max_length=100),
        ),
    ]
