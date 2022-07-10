from django.contrib import admin
from app_teacher.models import Receipt

# Register your models here.
admin.site.site_header = 'Панель управления приложением'
admin.site.index_title = 'Управление модели'
admin.site.site_title = 'Панель3'


class ReceiptAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Receipt' на панели администратора
    """

    list_display = (  # поля для отображения
        'title',
        'image',
        'description',
        'is_completed',
        'author',
        'time_to_cook',
        'instructions',
    )
    filter_horizontal = ('ingredients', 'category',)  # только для полей формата many_to_many_field
    list_display_links = (  # поля-ссылка
        'title',
        'description',
    )
    list_editable = (  # поля для редактирования объекта на лету
        'is_completed',
        'author',
        'time_to_cook',
    )
    list_filter = (  # поля для фильтрации
        'title',
        'image',
        'description',
        'is_completed',
        'author',
        'time_to_cook',
        'instructions',
    )
    fieldsets = (  # подзаголовки для визуального отделения блоков друг от друга
        ('Основное', {'fields': (
            'title',
            'description',
            'ingredients',
        )}),
        ('Дополнительно', {'fields': (
            'image',
            'category',
            'time_to_cook',
            'instructions',
        )}),
        ('Вспомогательное', {'fields': (
            'is_completed',
            'author',
        )}),
    )
    search_fields = [  # поле для поиска
        'title',
        'image',
        'description',
        'is_completed',
        'author',
        'time_to_cook',
        'instructions',
    ]


admin.site.register(Receipt, ReceiptAdmin)