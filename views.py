from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks = TaskModel.objects.all()

    form = TaskModelForm()

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo.html', context)

