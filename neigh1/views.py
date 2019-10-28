from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Nation,Neighborhood,Bussines
import json
import requests
from .forms import ProfileUpdateForm,BussinessForm
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
    buss_form=BussinessForm(instance=request.user.profile)
    form = ProfileUpdateForm(instance=request.user)
    context={
    'form':form,
    'buss_form':buss_form
    }
    return render(request,'setup.html',context)

@login_required
def add_type(request):
    if request.method == "GET":
        profile_pk = request.user.profile.pk
        profile = Profile.objects.get(pk = profile_pk)
        data = request.GET.get('set')
        profile.bussiness_type = data.capitalize()
        profile.save()
        return JsonResponse({'status':data})

def update_profile(request):
    if request.method == "POST":
        form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            form.user=request.user
            form.save()
        profile_pk = request.user.profile.pk
        profile = Profile.objects.get(pk = profile_pk)
        display_name = request.POST['display_name']
        phone_number = request.POST['phone_number']
        neighborhood = request.POST['neighborhood'].lower()
        email = request.POST['email']
        loc = Neighborhood.objects.filter(name__icontains = neighborhood).first()
        if loc == None:
            location = Neighborhood(name=neighborhood.capitalize(),occupants=0,registered_occupants=1)
            location.save()
            loc = location
        else:
            pass
        profile.profile_pic=form.cleaned_data['profile_pic']
        profile.display_name=display_name
        profile.phone_number=phone_number
        profile.email=email
        profile.neighborhood = loc
        profile.save()
        context={
        'profile':json.dumps(str(profile))
        }
        return redirect('/setup/')
    return redirect('/setup/')

def add_bussiness(request):
    if request.method == "POST":
        form = BussinessForm(request.POST,request.FILES,)
        if form.is_valid():
            form.save(commit=False)
            data=form.cleaned_data
            print(data['name'])
            buss=Bussines(name=data['name'],type=data['type'],bussiness_photo=data['bussiness_photo'],email=data['email'],phone_number=data['phone_number'])
            buss.profile= request.user.profile
            buss.save()
            return redirect('/')
