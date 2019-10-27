from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        exclude=('user','display_name','neighborhood','phone_number','email','bussiness_type','bussineses')
        fields=['profile_pic',]
