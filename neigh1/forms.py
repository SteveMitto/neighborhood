from django import forms
from .models import Profile,Bussines,NeighborhoodPost
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        exclude=('user','display_name','neighborhood','phone_number','email','bussiness_type','bussineses')
        fields=['profile_pic',]

class BussinessForm(forms.ModelForm):

    class Meta:
        model=Bussines
        exclude=('profile',)
        fields=('bussiness_photo','name','type','email','phone_number')

class NeigUsershPost(forms.ModelForm):

    class Meta:
        model=NeighborhoodPost
        exclude=('user',)
