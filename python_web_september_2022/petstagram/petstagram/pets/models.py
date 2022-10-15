from django.db import models
from django.utils.text import slugify

from petstagram.core.model_mixins import StrFromFieldMixin


class Pet(StrFromFieldMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30
    MAX_TYPE_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
        default='pet'
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.type}-{self.pk}")
        return super().save(*args, **kwargs)
