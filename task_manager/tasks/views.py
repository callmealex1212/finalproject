from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    search_query = request.GET.get('search')
    if search_query:
        tasks = Task.objects.filter(title__icontains=search_query)
    else:
        tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('index')

def dark_mode_toggle(request):
    return render(request, 'index.html', {})