
from .models import Album,Song
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from .forms import UserForm,AlbumForm,SongForm
from django.views.generic import View
from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import logout
from django.http import JsonResponse

def addalbum(request):
    if not request.user.is_authenticated():
        return render(request,'music/login.html')
    else:
        form = AlbumForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']
            album.save()
            return render(request,'music/detail.html',{'album':album})
        else:
            return render(request,'music/addalbum.html',{'form':form})


def updatealbum(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        album = get_object_or_404(Album, pk=album_id)
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            newobj = form.save(commit=False)
            newobj.album_logo = request.FILES['album_logo']
            album.artist = newobj.artist
            album.album_title = newobj.album_title
            album.genre = newobj.genre
            album.album_logo = request.FILES['album_logo']
            album.save()
            return render(request, 'music/detail.html', {'album': album})
        else:
            return render(request, 'music/updatealbum.html', {'form': form,'album':album})

def index(request):

    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        return render(request, 'music/index.html', {'albums': albums})

def detail(request,album_id):
    if not request.user.is_authenticated():
        return render(request,'music/login.html')
    else:
        album = get_object_or_404(Album,pk=album_id)
        return render(request,'music/detail.html',{'album':album})

def deletealbum(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request,'music/index.html',{'albums':albums})

def deletesong(request,album_id,song_id):
    album = get_object_or_404(Album,pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request,'music/detail.html',{'album':album})

def addsong(request,album_id):
    if not request.user.is_authenticated():
        return render(request,'music/login.html')
    else:
        album = get_object_or_404(Album,pk=album_id)
        if not request.user.is_authenticated():
            return render(request,'music/login.html')
        else:
            form = SongForm(request.POST or None,request.FILES or None)
            if form.is_valid():
                song = form.save(commit=False)
                song.album = album
                song.audio_file = request.FILES['audio_file']
                song.save()
                return render(request,'music/detail.html',{'album':album})
            else:
                return render(request,'music/addsong.html',{'form':form})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/registration_form.html', context)



def allsongs(request):
    all_albums = Album.objects.filter(user=request.user)
    return render(request,'music/allsongs.html',{'all_albums':all_albums})
def profile(request):
    if not request.user.is_authenticated():
        return render(request,'music/login.html')
    else:
        return render(request,'music/profile.html')

def logoutuser(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                albums = Album.objects.filter(user=request.user)
                return render(request,'music/index.html',{'albums':albums})
            else:
                return render(request,'music/login.html',{'error_message':'Your Accont has been disabled'})
        else:
            return render(request,'music/login.html',{'error_message':'You have entered either a wrong username and password. Login Again'})
    else:
        return render(request,'music/login.html',{'error_message':'Hello' })


def glanceall(request):
    if not request.user.is_authenticated():
        return render(request,'music/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        return render(request,'music/At_a_glance.html',{"albums":albums})


def getxml_foralbums(request):
    albums = Album.objects.filter(user=request.user)
    queryset = serializers.serialize('xml',albums)
    return HttpResponse(queryset,content_type="application/xml")

def getxml_forsongs(request,album_id):
    album_this = get_object_or_404(Album,pk=album_id)
    song = Song.objects.filter(album = album_this)
    queryset = serializers.serialize('xml',song)
    return HttpResponse(queryset,content_type="application/xml")

def getxml_forallsongs(request):
    albums = Album.objects.filter(user=request.user)
    songs = Song.objects.filter(album__in=albums)
    queryset = serializers.serialize('xml',songs)
    return HttpResponse(queryset,content_type="application/xml")
def getjson(request):
    albums = Album.objects.filter(user=request.user)
    queryset = serializers.serialize('json',albums)
    return HttpResponse(queryset,content_type="application/json")
def test_angular(request):
    return render(request,'music/test_angular.html')
