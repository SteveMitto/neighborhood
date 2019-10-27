from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Nation
import json
import requests
from .forms import ProfileUpdateForm
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    context={
    "form":form
    }
    return render(request,'registration/signup.html',context)
# Create your views here.

def index(request):

    return render(request,'index.html')
@login_required

def setup(request):
    form = ProfileUpdateForm(instance=request.user)
    return render(request,'setup.html',{'form':form})

@login_required
def add_type(request):
    if request.method == "GET":
        profile_pk = request.user.profile.pk
        profile = Profile.objects.get(pk = profile_pk)
        data = request.GET.get('set')
        print('*****************',data.capitalize())
        profile.bussiness_type = data.capitalize()
        profile.save()

        return JsonResponse({'status':data})


        # user = md.OneToOneField(User,on_delete=md.CASCADE)
        # profile_pic=md.ImageField(upload_to='profile_pic/',blank=True,null=True)
        # display_name=md.CharField(max_length =100,blank=True,null=True)
        # neighborhood = md.ForeignKey(Neighborhood,on_delete=md.PROTECT,related_name='people',blank=True,null=True)
        # phone_number = md.IntegerField(blank=True,null=True)
        # email = md.EmailField(blank=True,null=True)
        # bussiness_type=md.BooleanField(blank=True,null=True)
        # bussineses = md.ManyToManyField(Bussines,blank=True)

def update_profile(request):
    if request.method == "POST":
        form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            form.user=request.user
            form.save()
        else:
            print("*************Falied")
        profile_pk = request.user.profile.pk
        profile = Profile.objects.get(pk = profile_pk)
        display_name = request.POST['display_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        profile.profile_pic=form.cleaned_data['profile_pic']
        profile.display_name=display_name
        profile.phone_number=phone_number
        profile.email=email
        profile.save()
        context={
        'profile':json.dumps(str(profile))
        }
        return JsonResponse(context)
    return JsonResponse({'context':'SDAKLDJ'})
