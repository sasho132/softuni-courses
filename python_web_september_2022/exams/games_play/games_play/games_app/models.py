from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MAX_PASSWORD_LENGTH = 30
    MAX_NAME_LENGTH = 30

    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name='Email',
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(12)],
        verbose_name='Age',
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
        verbose_name='Password',
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )


class Game(models.Model):
    MAX_NAME_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    CATEGORIES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Title',
    )

    category = models.CharField(
        choices=CATEGORIES,
        max_length=CATEGORY_MAX_LENGTH,
        null=False,
        blank=False,
        verbose_name='Category',
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ],
        verbose_name='Rating',
    )

    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Max Level',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    summary = models.TextField(
        null=True,
        blank=True,
        verbose_name='Summary',
    )
