# Generated by Django 2.2.6 on 2019-10-29 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neigh1', '0023_auto_20191028_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhoodpost',
            name='user',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
