from django.core.validators import MinValueValidator
from django.db import models

from GamesPlayApp.games_play_app.validators import ValueInRangeValidator


class ProfileModel(models.Model):
    PASSWORD_MAX_LENGTH = 30
    NAME_MAX_LENGTH = 30
    AGE_MIN_VALUE = 12

    email = models.EmailField(
        verbose_name='Email',
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        verbose_name='Age',
        validators=(
          MinValueValidator(AGE_MIN_VALUE),
        ),
        blank=False,
        null=False,
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=PASSWORD_MAX_LENGTH,
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        blank=True,
        null=True,
    )


class GameModel(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        blank=False,
        null=False,
        max_length=TITLE_MAX_LENGTH,
        unique=True,
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=CATEGORY_MAX_LENGTH,
        blank=False,
        null=False,
    )

    rating = models.FloatField(
        blank=False,
        null=False,
        validators=(
          ValueInRangeValidator(0.1, 5.0),
        ),
    )

    max_level = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )
