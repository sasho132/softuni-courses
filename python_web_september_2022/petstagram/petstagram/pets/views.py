from django.shortcuts import render


def add_pet(request):
    return render(request, template_name='pet-add-page.html')


def edit_pet(request):
    return render(request, template_name='pet-edit-page.html')


def pet_details(request):
    return render(request, template_name='pet-details-page.html')


def delete_pet(request):
    return render(request, template_name='pet-delete-page.html')
