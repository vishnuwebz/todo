from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ToDoForm
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class TaskListView(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task1'

class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name="update.html"
    context_object_name='task'
    fields=('name','priority','date')

    #creating a url so while we click on update it will go to update page
    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('todoapp:cbvhome')


def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        #to save in database
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
# def details(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'task':task})

def delete(request,taskid):
    #fetch/get datas
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=ToDoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'task':task})
    # if request.method=='POST':
    #     task.update()
    #     return redirect('/')
    # return render(request,'edit.html',)
