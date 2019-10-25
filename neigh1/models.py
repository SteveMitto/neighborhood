from django.db import models as md

class Nation(md.Model):
    name = md.CharField(max_length=200)
    flag = md.URLField()

    class Meta:
        verbose_name = 'nation'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self):
        self.save()

class Town(md.Model):
    town = md.CharField(max_length = 200)
    nation = md.ForeignKey(Nation,on_delete =md.PROTECT)

    class Meta:
        verbose_name = 'town'
        ordering = ['nation']

    def __str__(self):
        return f'{self.town} in {self.nation}'

    def save(self):
        self.save()

class Neighborhood(md.Model):
    name = md.CharField(max_length=200)
    location = md.ForeignKey(Town,on_delete=md.CASCADE)
    occupants = md.IntegerField()
    registered_occupants = md.IntegerField()

    class Meta:
        verbose_name = 'nation'
        ordering = ['name']

    def save(self):
        self.save()
