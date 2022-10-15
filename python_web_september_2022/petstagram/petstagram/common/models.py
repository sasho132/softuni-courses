from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    MAX_COMMENT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_COMMENT_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
