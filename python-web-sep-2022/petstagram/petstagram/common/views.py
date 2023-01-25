from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_photo_id
from petstagram.photos.models import Photo


def index(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }
    return render(request, template_name='common/home-page.html', context=context)


def photo_like(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = PhotoLike(to_photo=photo)
        like.save()

    return redirect(get_photo_id(request, photo_id))


def photo_share(request, photo_id):
    # photo_details_url = reverse('details-photo', kwargs={
    #     'pk': photo_id,
    # })
    # copy(photo_details_url)

    copy(request.META['HTTP_HOST'] + resolve_url('details-photo', photo_id))

    return redirect(get_photo_id(request, photo_id))
