from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Todo
# Create your views here.


def create(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        print(todos)
        context = {
            "todos": todos,
        }
        return render(request, "create.html", context)
    else:
        return HttpResponse("Invalid request method", status=405)


def create(request):
    Todo.objects.create(content=request.POST["content"])
    return HttpResponse("create")


def create(request):
    return render(request, "create.html")
