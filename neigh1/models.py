from django.db import models as md
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class Nation(md.Model):
    name = md.CharField(max_length=200)
    flag = md.URLField()
    calling_codes =md.CharField(max_length=100,blank=True,null=True)
    currency=md.CharField(max_length=100,blank=True,null=True)
    symbol=md.CharField(max_length=10,blank=True,null=True)


    class Meta:
        verbose_name = 'nation'
        ordering = ['name']

    def __str__(self):
        return self.name


class Town(md.Model):
    town = md.CharField(max_length = 200)
    nation = md.ForeignKey(Nation,on_delete =md.PROTECT , related_name='towns')

    class Meta:
        verbose_name = 'town'
        ordering = ['nation']

    def __str__(self):
        return f'{self.nation} -> {self.town}'


class Neighborhood(md.Model):
    name = md.CharField(max_length=200)
    location = md.ForeignKey(Town,default=1,on_delete=md.CASCADE,related_name='neighborhoods')
    occupants = md.IntegerField()
    registered_occupants = md.IntegerField()

    class Meta:
        verbose_name = 'neighborhood'
        ordering = ['name']

    def __str__(self):
        return self.name

class Profile(md.Model):
    user = md.OneToOneField(User,on_delete=md.CASCADE)
    profile_pic=md.ImageField(upload_to='profile_pic/',blank=True,null=True)
    display_name=md.CharField(max_length =100,blank=True,null=True)
    neighborhood = md.ForeignKey(Neighborhood,on_delete=md.PROTECT,related_name='people',blank=True,null=True)
    phone_number = md.IntegerField(blank=True,null=True)
    email = md.EmailField(blank=True,null=True)
    bussiness_type=md.BooleanField(blank=True,null=True)

    class Meta:
        verbose_name='profile'
        ordering=['user']

    def __str__(self):
        return f"{self.user}'s profile"

class Bussines(md.Model):
    name = md.CharField(max_length=255)
    type = md.CharField(max_length=150)
    bussiness_photo = md.ImageField(upload_to='bussiness_pics/',default="bussiness_pics/no-photo.jpg")
    email = md.EmailField()
    phone_number = md.IntegerField()
    profile =md.ForeignKey(Profile,on_delete=md.CASCADE,related_name="bussines")

    class Meta:
        verbose_name='bussines'
        ordering=['name']

    def __str__(self):
        return f'{self.neighborhood} -> {self.name}'
