from django.db import models as md

class Nation(md.Model):
    name = md.CharField(max_length=200)
    flag = md.URLField()
    calling_codes =md.IntegerField()
    currency=md.CharField(max_length=100)
    symbol=md.CharField(max_length=10)


    class Meta:
        verbose_name = 'nation'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self):
        self.save()

class Town(md.Model):
    town = md.CharField(max_length = 200)
    nation = md.ForeignKey(Nation,on_delete =md.PROTECT , related_name='towns')

    class Meta:
        verbose_name = 'town'
        ordering = ['nation']

    def __str__(self):
        return f'{self.nation} -> {self.town}'

    def save(self):
        self.save()

class Neighborhood(md.Model):
    name = md.CharField(max_length=200)
    location = md.ForeignKey(Town,on_delete=md.CASCADE,related_name='neighborhoods')
    occupants = md.IntegerField()
    registered_occupants = md.IntegerField()

    class Meta:
        verbose_name = 'neighborhood'
        ordering = ['name']

    def save(self):
        self.save()

    def __str__(self):
        return self.name

class Bussines(md.Model):
    name = md.CharField(max_length=255)
    type = md.CharField(max_length=150)
    neighborhood = md.ForeignKey(Neighborhood,on_delete=md.PROTECT)
    email = md.EmailField()
    phone_number = md.IntegerField()

    class Meta:
        verbose_name='bussines'
        ordering=['name']

    def save(Self):
        self.save()

    def __str__(self):
        return f'{self.neighborhood} -> {self.name}'
