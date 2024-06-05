from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(req):
    task1 = Task.objects.all()
    if req.method == 'POST':
        name = req.POST.get('task','')
        priority = req.POST.get('priority','')
        date = req.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()

    return render(req, "task_list.html",{'task1':task1})


def task_update(req,id):
    task = Task.objects.get(id = id)
    f = TaskForm(req.POST or None,instance = task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req,'task_update.html',{'f':f,'task':task})

def task_delete(req,id):
    task = Task.objects.get(id = id)
    if req.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(req,'task_delete.html',{'task':task})