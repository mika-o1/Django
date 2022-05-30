from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


def my_index(request):
    return render(request, 'app_student/pages/my_index.html')


def my_home(request):
    return render(request, 'app_student/pages/my_home.html')


def my_about(request):
    return render(request, 'app_student/pages/my_about.html')


def my_origin_home(request):
    return render(request, 'app_student/pages/my_origin_home.html')


def my_todo_detail(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    context = {
        "todo": obj
    }
    return render(request, 'app_student/pages/my_todo_detail.html', context)


def my_todo_list(request):
    obj = models.Task.objects.all()
    context = {"list": obj}
    return render(request, 'app_student/pages/my_todo_list.html', context)


def my_todo_create(request):
    if request.method == "POST":
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")
        obj = models.Task.objects.create(
            title=title1,
            description=description1
        )
        obj.save()
    context = {}
    return render(request, 'app_student/pages/my_todo_create.html', context)


def my_todo_delete(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    obj.delete()
    return redirect(reverse('my_todo_list', args=()))


def my_todo_update_status(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    # obj.is_completed = not obj.is_completed
    if obj.is_completed:
        obj.is_completed = False
    else:
        obj.is_completed = True
    obj.save()
    return redirect(reverse('my_todo_list', args=()))


def my_todo_change_data(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)

    if request.method == "POST":
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")
        if obj.title != title1:
            obj.title = title1
        if obj.description != description1:
            obj.description = description1
        obj.save()
    context = {
        "todo": obj
    }
    return render(request, 'app_student/pages/my_todo_change.html', context)
