from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


# тут только "логика" - функции для обработки и возврат данных

def index(request):
    return render(request, 'app_teacher/pages/index.html')


def home(request):
    return render(request, 'app_teacher/pages/home.html')


def about(request):
    return render(request, 'app_teacher/pages/about.html')


def origin_home(request):
    return render(request, 'app_teacher/pages/origin_home.html')


def todo_detail(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    context = {
        "todo": obj
    }
    return render(request, 'app_teacher/pages/DetailTodo.html', context)


def todo_list(request):
    obj = models.Task.objects.all()
    context = {"list": obj}
    return render(request, 'app_teacher/pages/todo_list.html', context)


def todo_create(request):
    if request.method == "POST":
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")
        obj = models.Task.objects.create(
            title=title1,
            description=description1
        )
        obj.save()
    context = {}
    return render(request, 'app_teacher/pages/CreateTodo.html', context)


def todo_delete(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    obj.delete()
    return redirect(reverse('todo_list', args=()))


def todo_update_status(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    # obj.is_completed = not obj.is_completed
    if obj.is_completed:
        obj.is_completed = False
    else:
        obj.is_completed = True
    obj.save()
    return redirect(reverse('todo_list', args=()))

