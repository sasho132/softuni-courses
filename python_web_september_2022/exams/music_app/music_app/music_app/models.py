from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models


class ProfileModel(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            MaxLengthValidator(MAX_USERNAME_LENGTH),
        ],

        null=False,
        blank=False,
        max_length=MAX_USERNAME_LENGTH,
    )

    email = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class AlbumModel(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_PRICE_VALUE = 0.0
    GENRE_CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )

    album_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_NAME_LENGTH,
        choices=GENRE_CHOICES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[MinValueValidator(MIN_PRICE_VALUE)]
    )
