from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from . import forms 

def home_page(request):
    return HttpResponse("Home page")

def todo(request):
    query_set = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': query_set})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Todo deleted successfully', extra_tags='success')
    return redirect('todo')

def create(request):
    if request.method == 'POST':
        form = forms.TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created_at=cd['created_at'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('todo')
    else:
        form = forms.TodoCreateForm()

    return render(request, 'create.html', {'form':form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = forms.TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Updated successfully', 'success')
            return redirect('detail', todo_id)
    else:
        form = forms.TodoUpdateForm(instance=todo)

    return render(request, 'update.html', {'form':form})



