from django.shortcuts import render, redirect
from .forms import RegisterForm
from tasks.models import Task
from tasks.forms import TaskForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

@login_required
def dashboard(request):
    if request.user.is_staff:
        message = "Admin User"
    else:
        message = "Regular User"

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    return render(
        request,
        "dashboard.html",
        {
            "tasks": tasks,
            "form": form,
            "message": message
        }
    )

def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect("dashboard")