from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Nation,Neighborhood,Bussines,NeighborhoodPost,ChatKey,RealChat
import json
import requests
from .forms import ProfileUpdateForm,BussinessForm,NeigUsershPost
import json
import secrets
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
@login_required
def index(request):
    neighbor = request.user.profile.neighborhood
    hospital = Bussines.objects.filter(type__icontains="hospital" ,profile__neighborhood = neighbor).all()
    police = Bussines.objects.filter(type__icontains="police" ,profile__neighborhood = neighbor).all()
    bussinesses = Bussines.objects.filter(profile__neighborhood = neighbor).all()
    neighbourhood_post=NeighborhoodPost.objects.filter(user__profile__neighborhood = neighbor).all()
    my_neighboors = Profile.objects.filter(neighborhood = neighbor).all()
    post_form=NeigUsershPost(instance=request.user)
    context={
    "neighbors":my_neighboors.exclude(user = request.user),
    "post_form":post_form,
    "neighbourhood_post":neighbourhood_post,
    "neighborhood":neighbor,
    "bussinesses":bussinesses,
    "hospital":hospital,
    "police":police,
    }
    return render(request,'index.html',context)

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

def neig_post_save(request):
    if request.method == "POST":
        post_form=NeigUsershPost(request.POST,request.FILES)
        if post_form.is_valid():
            print(request.user.pk)
            form=post_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')

def chating_validate(request,username):
    '''
        This function checks if a certain chart have the chart token and returns
        the chart token to a
    '''
    user1 = request.user
    user2=User.objects.filter(username=username).first()
    if user2 == user1:
        return redirect('/')
    chat_key_available=ChatKey.objects.filter(user1=user1, user2=user2).first()
    chat_key_available2=ChatKey.objects.filter(user1=user2, user2=user1).first()
    if chat_key_available == None:
        if chat_key_available2 == None:
            new_token = secrets.token_hex(16)
            token_query = ChatKey.objects.filter(chat_token=new_token).first()
            while token_query != None:
                new_token = secretes.token_hex(16)
            new_chat = ChatKey(user1=user1,chat_token=new_token,user2=user2)
            new_chat.save()
            return new_chat.chat_token
        else:
            return chat_key_available2.chat_token
    return chat_key_available.chat_token


def chating(request,username):
    receiver=User.objects.filter(username=username).first()
    users_chat_token=chating_validate(request,username)
    chats=RealChat.objects.filter(chat_token = users_chat_token).all()
    if request.method == "POST":
        message = request.POST['sent_message']
        new_msg=RealChat(chat_user1=request.user,chat_user2=receiver,chat_token=users_chat_token,message=message,chat_sender=request.user)
        new_msg.save()
    context={
    "chats":chats,
    "receiver":receiver
    }
    # return JsonResponse(json.dumps(str(users_chat_token)),safe=False)
    return render(request,'chat.html',context)
