from django.db.models.signals import pre_save
from django.dispatch import receiver
from transliterate import translit
from django.utils.text import slugify

from .models import Note


@receiver(pre_save, sender=Note)
def add_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(translit(instance.title, 'ru', reversed=True))