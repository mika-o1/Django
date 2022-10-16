# Generated by Django 4.0.4 on 2022-06-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_teacher', '0008_receiptingredient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receiptingredient',
            options={'ordering': ('name',), 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AddField(
            model_name='receipt',
            name='ingredients',
            field=models.ManyToManyField(blank=True, default=None, help_text='<small class="text-muted">ингредиенты</small><hr><br>', null=True, to='app_teacher.receiptingredient', verbose_name='Ингредиенты блюда'),
        ),
    ]