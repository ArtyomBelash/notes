from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return f'profiles/{instance.username}/{filename}'


def get_slug(instance):
    return f'{instance.username}'


class Profile(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, validators=[EmailValidator()])
    picture = models.ImageField('Фото', upload_to=upload_to, default='profiles/default/img.png')
    slug = models.SlugField('URl', db_index=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
