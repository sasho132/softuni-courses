from django.db import models


class Profile(models.Model):
    MAX_NAMES_LENGTH = 20

    first_name = models.CharField(
        max_length=MAX_NAMES_LENGTH,
        null=False,
        blank=False,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_NAMES_LENGTH,
        null=False,
        blank=False,
        verbose_name='Last Name',
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Age',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to Profile Image'
    )


class Note(models.Model):
    MAX_NAME_LENGTH = 30

    title = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name='Title',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    content = models.TextField(
        null=False,
        blank=False,
        verbose_name='Content',
    )
