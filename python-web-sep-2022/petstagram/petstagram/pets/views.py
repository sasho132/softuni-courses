from django.shortcuts import render

from petstagram.pets.utils import get_pet_by_name_and_username


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def edit_pet(request, username, pet_slug):
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, template_name='pets/pet-delete-page.html')


def details_pet(request, pet_slug, username):
    pet = get_pet_by_name_and_username(pet_slug, username)

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': pet.photo_set.all(),
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)
