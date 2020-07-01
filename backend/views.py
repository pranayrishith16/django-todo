from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def home(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
    form = TodoForm()
    todo_s = Todo.objects.all()
    todo_list = []
    for todo in todo_s:
        todo_list.append(todo)

    dict = {'todo_list': todo_list, 'form': form}
    return render(request, 'backend/index.html', dict)


def delete_todo(request, todo_id):
    todo_delete = Todo.objects.get(id=todo_id)
    todo_delete.delete()
    return redirect('home')
