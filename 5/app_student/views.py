from django.shortcuts import render
from app_teacher import models


def my_todo_list(request):
    obj = models.Task.objects.all()
    context = {"list": obj}
    return render(request, 'app_student/pages/my_todo_list.html', context)


# def my_todo_detail(request, todo_id):
#     obj = models.Task.objects.get(id=todo_id)
#     context = {
#         "todo": obj
#     }
#     return render(request, 'app_teacher/pages/my_todo_detail.html', context)
#
#
# def my_todo_create(request):
#     if request.method == "POST":
#         title1 = request.POST.get("title", "заголовок по умолчанию")
#         description1 = request.POST.get("description", "описание по умолчанию")
#         obj = models.Task.objects.create(
#             title=title1,
#             description=description1
#         )
#         obj.save()
#     context = {}
#     return render(request, 'app_teacher/pages/my_todo_create.html', context)