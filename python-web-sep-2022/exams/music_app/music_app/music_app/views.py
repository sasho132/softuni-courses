from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from MusicApp.music_app.forms import CreateProfileForm, CreateAlbumForm, DeleteAlbumForm
from MusicApp.music_app.models import ProfileModel, AlbumModel


def index(request):
    profile = ProfileModel.objects.first()
    if profile:
        albums = AlbumModel.objects.all()
        context = {
            'profile': profile,
            'albums': albums,
        }
        return render(request, 'home-with-profile.html', context)

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def album_add(request):
    profile = ProfileModel.objects.first()
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = AlbumModel.objects.filter(pk=pk).get()
    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = AlbumModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CreateAlbumForm(initial=album.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'edit-album.html', context)

    else:
        form = CreateAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = AlbumModel.objects.filter(pk=pk).get()
    profile = ProfileModel.objects.first()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
        contex = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'delete-album.html', contex)

    album.delete()
    return redirect('home-page')


def profile_details(request):
    profile = ProfileModel.objects.first()
    albums = AlbumModel.objects.all()
    total_albums = len(albums)

    context = {
        'profile': profile,
        'albums': albums,
        'total_albums': total_albums,
    }

    return render(request, 'profile-details.html', context)


def profile_delete(request):
    if request.method == 'POST':
        profile = ProfileModel.objects.first()
        albums = AlbumModel.objects.all()
        profile.delete()
        albums.delete()
        return redirect('home-page')

    return render(request, 'profile-delete.html')
