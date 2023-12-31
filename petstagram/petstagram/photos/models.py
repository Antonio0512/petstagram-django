from django.db import models
from django.core.validators import MinLengthValidator

from ..accounts.models import PetstagramUser
from ..pets.models import Pet
from .validators import validate_file_size


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='images',
        validators=(validate_file_size,)
    )
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True
    )
    date_published = models.DateField(
        auto_now=True
    )

    user = models.ForeignKey(
        PetstagramUser,
        on_delete=models.RESTRICT
    )
