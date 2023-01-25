from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.model_mixins import StrFromFieldMixin
from petstagram.pets.models import Pet
from petstagram.photos.validator import validate_file_size


class Photo(StrFromFieldMixin, models.Model):
    str_fields = ('pk', 'date_of_publication')

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        validators=(validate_file_size,),
        upload_to='./mediafiles/photos',
        null=False,
        blank=True,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
        blank=True,
        null=False,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
