from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out,user_logged_in
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_out)
def remove_online_status(request,**kwargs):
    p_pk = request.user.profile.pk
    online_status=Profile.objects.get(pk = p_pk)
    online_status.online=False
    online_status.save()

@receiver(user_logged_in)
def add_online_status(request,**kwargs):
    p_pk = request.user.profile.pk
    online_status=Profile.objects.get(pk = p_pk)
    online_status.online=True
    online_status.save()
