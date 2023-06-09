from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import TodoForm
from django.utils import timezone
from django.template import RequestContext

def index(request):
    return get_todolist(request, todolist_id=1)

def get_todolist(request, todolist_id):
    todolists = Todolist.objects.all()
    todos = Todo.objects.filter(fk_todo_todolist=todolist_id).order_by('priority')
    name_list = Todolist.objects.get(id=todolist_id)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data   
            data.update({'fk_todo_todolist': name_list})
            data.update({'complete_date':None})
            todo = Todo(**data)
            todo.save()
            return redirect('todolist', name_list.id)
    else:
        form = TodoForm()
    context = {
        'todolists': todolists,
        'todos':todos,
        'high': HIGH,
        'medium': MEDIUM,
        'low': LOW,
        'name_list':name_list,
        'form':form
    }
    return render(request, "index.html", context)


def update_todo(request, todolist_id, todo_id):
    todolists = Todolist.objects.all()
    todos = Todo.objects.filter(fk_todo_todolist=todolist_id).order_by('priority')
    name_list = Todolist.objects.get(id=todolist_id)
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.update({'id': todo_id})   
            data.update({'fk_todo_todolist': name_list})
            data.update({'complete_date':None})
            todo = Todo(**data)
            todo.save()
            return redirect('todolist', name_list.id)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todolists': todolists,
        'todos':todos,
        'high': HIGH,
        'medium': MEDIUM,
        'low': LOW,
        'name_list':name_list,
        'form':form,
        'todo_id':todo_id
    }
    return render(request, "update_todo.html", context)


def delete_todo(request, todolist_id, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todolist', todolist_id)

def delete_todolist(request, todolist_id):
    todolist = Todolist.objects.get(id=todolist_id)
    todolist.delete()
    return redirect('index')
    
def done_todo(request, todolist_id, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete_date = timezone.now()
    todo.priority = None
    todo.save()
    return redirect('todolist', todolist_id)            

def handler404(request, *args, **argv):
    response = render(request, '404.html')
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render(request, '500.html')
    response.status_code = 500
    return response
