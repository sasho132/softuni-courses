from django.shortcuts import render, redirect

from OnlineLibrary.library_app.forms import CreateProfileForm, CreateBookFrom, DeleteProfileForm
from OnlineLibrary.library_app.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def get_first_profile():
    return Profile.objects.first()


def get_books():
    books = Book.objects.all()
    book_chunks = [books[x:x + 3] for x in range(0, len(books), 3)]
    return book_chunks


def delete_book(pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home-page')


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    books = get_books()

    profile = Profile.objects.first()
    context = {
        'books': books,
        'profile': profile,
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


def add_book(request):
    if request.method == 'GET':
        form = CreateBookFrom()
    else:
        form = CreateBookFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
        'profile': get_first_profile()
    }

    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = CreateBookFrom(instance=book)
    else:
        form = CreateBookFrom(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
        'profile': get_first_profile(),
        'book': book,
    }

    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book,
        'profile': get_first_profile(),
        'delete_book': delete_book(pk=pk),
    }

    return render(request, 'book-details.html', context)


def profile_details(request):
    profile = get_first_profile()
    profile_full_name = f"{profile.first_name} {profile.last_name}"

    context = {
        'profile': profile,
        'full_name': profile_full_name,
    }

    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = get_first_profile()

    if request.method == 'GET':
        form = CreateProfileForm(instance=profile)
    else:
        form = CreateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'form': form,
        'profile': get_first_profile()
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_first_profile()
    books = Book.objects.all()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            books.delete()
            return redirect('home-page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)
