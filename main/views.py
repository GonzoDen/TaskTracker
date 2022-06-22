#base urls file

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')[:5]
    return render(request, 'main/index.html', {'title':'Main page', 'tasks':tasks})


def about(request):
    return render(request, 'main/about.html')

def newtodo(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/newtodo.html', context)
