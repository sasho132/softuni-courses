from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from notes.notes_app.forms import CreateProfileForm, CreateNoteForm, DeleteNoteForm
from notes.notes_app.models import Profile, Note


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    profile = Profile.objects.first()
    all_notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': all_notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_profile(request):
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


def add_note(request):
    if request.method == 'GET':
        form = CreateNoteForm()
    else:
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        form = CreateNoteForm(instance=note)
    else:
        form = CreateNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    profile_full_name = f"{profile.first_name} {profile.last_name}"
    all_notes = len(Note.objects.all())

    context = {
        'profile': profile,
        'full_name': profile_full_name,
        'all_notes': all_notes,
    }

    return render(request, 'profile.html', context)
