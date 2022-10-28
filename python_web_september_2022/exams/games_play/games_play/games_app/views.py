from django.shortcuts import render, redirect

from games_play.games_app.forms import CreateProfile, CreateGame, DeleteGame, EditProfile, DeleteProfile
from games_play.games_app.models import Profile, Game


def games_average_rating():
    games = Game.objects.all()
    total_scores = sum([game.rating for game in games])

    try:
        average_rating = total_scores / len(games)
    except ZeroDivisionError:
        average_rating = 0.0
    return average_rating


def get_profile_names(profile_pk):
    profile = Profile.objects.filter(pk=profile_pk).get()

    profile_names = [profile.first_name, profile.last_name]
    res = [name for name in profile_names if name is not None]
    return ' '.join(res)


def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = Profile.objects.first()

    context = {
        'games': games,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)


def game_create(request):
    if request.method == 'GET':
        form = CreateGame()
    else:
        form = CreateGame(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-game.html', context)


def game_details(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }

    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CreateGame(instance=game)
    else:
        form = CreateGame(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteGame(instance=game)
    else:
        form = DeleteGame(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'delete-game.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfile()
    else:
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    total_games = len(Game.objects.all())

    context = {
        'profile': profile,
        'profile_names': get_profile_names(profile.pk),
        'average_rating': games_average_rating(),
        'total_games': total_games,
    }

    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = EditProfile(instance=profile)
    else:
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    if request.method == 'GET':
        form = DeleteProfile(instance=profile)
    else:
        form = DeleteProfile(request.POST, instance=profile)
        if form.is_valid():
            games.delete()
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
