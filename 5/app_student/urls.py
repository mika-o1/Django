from django.urls import path
# from .views import home, index, about, todo_detail
from . import views as logic

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path(route='my_todo_list/', view=logic.my_todo_list, name="my_todo_list"),
    # path('my_todo_detail/<int:todo_id>/', my_todo_detail, name="my_todo_detail"),
    # path(route='my_todo_create/', view=logic.my_todo_create, name="my_todo_create"),
]