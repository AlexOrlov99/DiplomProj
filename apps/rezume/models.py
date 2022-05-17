from datetime import datetime
import re

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
    FileField,
    EmailField,
    DateField,
    ImageField,
    PROTECT,
    CASCADE,
)
from abstracts.models import AbstractDateTime
from auths.models import CustomUser

class FileQuerySet(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )

class File(AbstractDateTime):

    FILE_TYPE = 'docx'

    title = CharField(
        verbose_name='Название файла',
        max_length=50,
    )
    obj = FileField(
        verbose_name='Объект документа',
        upload_to='rezume_files/%Y/%m/%d',
        max_length=255
    )
    objects = FileQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    

class RezumeQuerySet(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )


class Resume(AbstractDateTime):

    file = OneToOneField(
        File,
        verbose_name='вложенный файл',
        on_delete=CASCADE,
    )
    full_name = CharField(
        max_length=50,
        verbose_name='Полное имя',
    )
    email = EmailField(
        verbose_name='Почта/Логин', 
        unique=True,
    )
    phone_number = CharField(
        max_length=20,
        verbose_name='Номер телефона',
        null=True,
        blank=True,
    )
    education = TextField(
        verbose_name='Образование',
        default='',       
    )
    skills = TextField(
        verbose_name='Проффесиональные навыки',
        default='',
    )
    experience = TextField(
        verbose_name='Проффесиональные навыки',
        default='',
    )

    objects = RezumeQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.full_name} | {self.email}'

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save(
            update_field=['datetime_deleted']
        )

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'