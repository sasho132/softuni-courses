from django.http import HttpResponse
from django.shortcuts import render, redirect

from GamesPlayApp.games_play_app.forms import ProfileCreateForm, GameCreateForm, DeleteGameForm, EditProfileForm
from GamesPlayApp.games_play_app.models import GameModel, ProfileModel


def index(request):
    profile = ProfileModel.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def dashboard(request):
    games = GameModel.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'dashboard.html', context)


def game_create(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-game.html', context)


def game_details(request, pk):
    game = GameModel.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    game = GameModel.objects.filter(pk=pk).get()
    form = GameCreateForm(initial=game.__dict__)

    if request.method == 'GET':
        context = {
            'form': form,
        }
        return render(request, 'edit-game.html', context)

    form = GameCreateForm(request.POST, instance=game)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    else:
        context = {
            'form': form,
        }
        return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = GameModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
        context = {
            'form': form,
        }
        return render(request, 'delete-game.html', context)

    game.delete()
    return redirect('dashboard')


def profile_details(request):
    profile = ProfileModel.objects.first()
    all_games = GameModel.objects.all()
    total_games = len(all_games)

    try:
        average_rating = sum([game.rating for game in all_games]) / total_games
    except ZeroDivisionError:
        average_rating = 0

    context = {
        'profile': profile,
        'average_rating': average_rating,
        'total_games': total_games,
    }

    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = ProfileModel.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(initial=profile.__dict__)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    games = GameModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('index')

    return render(request, 'delete-profile.html')
