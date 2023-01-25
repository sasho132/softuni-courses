from django.core.exceptions import ValidationError

from petstagram.core.utils import megabytes_to_bytes


def validate_file_size(obj):
    filesize = obj.file.size
    megabyte_limit = 5.0

    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
