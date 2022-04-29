from datetime import datetime

from django.db.models import (
    Model,
    QuerySet,
    ManyToManyField,
    ForeignKey,
    OneToOneField,
    CharField,
    TextField,
    IntegerField,
    DateTimeField,
    PROTECT,
    CASCADE,
)

from abstracts.models import AbstractDateTime


class Rezume(AbstractDateTime):

    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        )
    surname = models.CharField(
        max_length=50,
        verbose_name='Имя',
        )

    obj = models.FileField(
        upload_to='rezume_files/%Y%m',
        verbose_name='Файл'
        )
    