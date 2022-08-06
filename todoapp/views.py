from django.shortcuts import render, redirect
from .models import Task
# from django.views.generic import DeleteView
# from django.urls import reverse_lazy
from .forms import Todoforms


# from django.views.generic import UpdateView


# from django.shortcuts import HttpResponse


# Create your views here.


def home(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        # date = request.POST.get('date')
        obj = Task(name=name, priority=priority)
        obj.save()
    return render(request, 'home.html', {'obj1': obj1})


# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('cbvtask')


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})


# class TaskUpdateView(UpdateView):
#     model = Task
#     templates_name = 'update.html'
#     context_object_name = 'task'
#     fields = ('name', 'priority', 'date')


def update(request, id):
    task = Task.objects.get(id=id)
    form = Todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'task': task, 'form': form})
# def home(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = Task(name=name, priority=priority)
#         obj.save()
#     return render(request, "task.html")
