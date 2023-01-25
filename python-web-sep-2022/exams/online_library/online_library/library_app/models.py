from django.db import models


class Profile(models.Model):
    MAX_NAMES_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_NAMES_LENGTH,
        null=False,
        blank=False,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_NAMES_LENGTH,
        null=False,
        blank=False,
        verbose_name='Last Name'
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )


class Book(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_TYPE_LENGTH = 30

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
    )
