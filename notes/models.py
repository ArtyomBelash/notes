from django.db import models
from profiles.models import Profile


class Note(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    date_of_creation = models.DateTimeField('Дата создания', auto_now_add=True)
    date_of_update = models.DateTimeField('Дата обновления', auto_now=True)
    slug = models.SlugField('URL', unique=True, db_index=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Владелец', related_name='notes')

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'
        db_table = 'note'
        ordering = ('-date_of_update',)
