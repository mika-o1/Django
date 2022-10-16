# Generated by Django 4.0.6 on 2022-08-25 16:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_profile_profile2'),
        ('backend_api', '0008_modelbook_created_datetime_field_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBookRating',
            fields=[
                ('user', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">Аккаунт</small><hr><br>', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Аккаунт')),
                ('rating', models.IntegerField(blank=True, default=1, help_text='<small class="text-muted"></small><hr><br>', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Время на чтение')),
                ('book', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">Книга</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_api.modelbook', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Рейтинг книги',
                'verbose_name_plural': 'Рейтинг книг',
                'ordering': ('book',),
            },
        ),
    ]
