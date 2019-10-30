# Generated by Django 2.2.6 on 2019-10-29 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neigh1', '0034_auto_20191029_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realchat',
            old_name='sender',
            new_name='chat_user1',
        ),
        migrations.RenameField(
            model_name='realchat',
            old_name='receiver',
            new_name='chat_user2',
        ),
        migrations.AddField(
            model_name='realchat',
            name='chat_sender',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, related_name='sent', to=settings.AUTH_USER_MODEL),
        ),
    ]