from django.db import models

from recipes.recipes_app.validators import ingredients_split


class Recipe(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_INGREDIENTS_LENGTH = 250

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
        verbose_name='Title',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Description',
    )

    ingredients = models.CharField(
        max_length=MAX_INGREDIENTS_LENGTH,
        null=False,
        blank=False,
        verbose_name='Ingredients',
        validators=[ingredients_split]
    )

    time = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Time (Minutes)',
    )
