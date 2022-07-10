from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.


class Receipt(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=250,
    )
    image = models.ImageField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="media/recept/default/default_receipt.jpg",
        verbose_name="Заставка:",
        help_text='<small class="text-muted">это наша заставка</small><hr><br>',

        validators=[FileExtensionValidator(['jpg', 'png'])],
        max_length=100,
    )
    description = models.TextField(
        unique=False,
        # editable=
    )
    is_completed = models.BooleanField(
        default=False,
        # editable=
    )

    class Meta:
        app_label = 'app_teacher'
        ordering = ('title', 'description')
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.title} [{self.id}]'

    def return_clear_data(self):
        title = self.title
        return str(title).strip() + " banana"

