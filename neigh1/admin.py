from django.contrib import admin
from .models import Profile ,Nation,Town,Neighborhood,Bussines,NeighborhoodPost,ChatKey,RealChat
# Register your models here.
admin.site.register(Profile)
admin.site.register(Nation)
admin.site.register(Town)
admin.site.register(Neighborhood)
admin.site.register(Bussines)
admin.site.register(NeighborhoodPost)
admin.site.register(ChatKey)
admin.site.register(RealChat)
