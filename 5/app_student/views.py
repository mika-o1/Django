from django.shortcuts import render
from app_teacher import models


def my_todo_list(request):
    obj = models.Task.objects.all()
    context = {"list": obj}
    return render(request, 'app_student/pages/my_todo_list.html', context)


