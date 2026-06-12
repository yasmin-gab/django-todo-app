from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    total_tasks = len(tasks)
    completed_tasks = 0
    remaining_tasks = 0
    percentage = 0

    for task in tasks:
        if task.done == True:
            completed_tasks += 1
    
    remaining_tasks = total_tasks - completed_tasks
    
    if total_tasks > 0:
        percentage = int((completed_tasks / total_tasks) * 100)
            
    return render(
        request, 
        'tasks/home.html',
        {
            'tasks': tasks,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'remaining_tasks': remaining_tasks,
            'percentage': percentage
        }
        )

def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        
    return redirect('home')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.done == True:
        task.done = False
    else:
        task.done = True
    
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect('home')