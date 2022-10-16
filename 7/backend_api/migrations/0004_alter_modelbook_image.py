# Generated by Django 4.0.6 on 2022-08-02 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0003_alter_modelbook_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbook',
            name='image',
            field=models.ImageField(blank=True, default='default/modelbooks/default_book.jpg', help_text='<small class="text-muted">это наша заставка</small><hr><br>', null=True, upload_to='modelbooks', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'bmp', 'jpeg'])], verbose_name='Заставка:'),
        ),
    ]
