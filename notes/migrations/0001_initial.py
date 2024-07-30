# Generated by Django 5.0.7 on 2024-07-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_of_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Записка',
                'verbose_name_plural': 'Записки',
                'db_table': 'note',
                'ordering': ('-date_of_update',),
            },
        ),
    ]