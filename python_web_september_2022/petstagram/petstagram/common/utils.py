def get_photo_id(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
